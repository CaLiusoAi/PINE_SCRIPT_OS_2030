#!/usr/bin/env python3
"""PINE PREFLIGHT v1.0 — mechanical gate for Pine v6 emissions.
Encodes every error class hit in-session plus the canon's session-killers.
Usage: python3 pine_preflight.py <script.pine.txt>
Exit 0 = all gates pass. Exit 1 = violations (emission forbidden).
Rule IDs cite PSv6 MASTER FAILURE TAXONOMY v3.1 / AIO v3.1 laws.
"""
import re, sys

def lint(text):
    lines = text.split("\n")
    v = []  # (rule_id, line_no, message)

    # G01 — //@version=6 must be the first line (L1 / Ω-ONE Law 1)
    _l1 = lines[0].strip() if lines else ""
    import re as _re
    _vm = _re.match(r"//@version=(\d+)", _l1)
    if _vm and _vm.group(1) != "6":
        v.append(("G01:VERSION_NOT_6", 1, f"//@version={_vm.group(1)} — canon requires v6; rewrite for v6"))
    elif _l1 != "//@version=6":
        v.append(("G01:VERSION_FIRST", 1, "//@version=6 must be line 1 exactly"))

    # G02 — exactly one declaration statement
    decls = [i for i, l in enumerate(lines, 1)
             if re.match(r"\s*(indicator|strategy|library)\s*\(", l)]
    if len(decls) != 1:
        v.append(("G02:ONE_DECLARATION", decls[1] if len(decls) > 1 else 1,
                  f"need exactly 1 declaration, found {len(decls)}"))
    is_strategy = any(re.match(r"\s*strategy\s*\(", lines[d-1]) for d in decls)

    # G03 — shorttitle <= 10 chars (SHORT_TITLE_TOO_LONG — hit in-session)
    for i, l in enumerate(lines, 1):
        m = re.search(r'(?:indicator|strategy)\s*\(\s*"[^"]*"\s*,\s*"([^"]*)"', l)
        if m and len(m.group(1)) > 10:
            v.append(("G03:SHORT_TITLE", i, f'shorttitle "{m.group(1)}" is {len(m.group(1))} chars (max 10)'))

    # Build bool symbol table: declared bool, assigned true/false, or assigned
    # a comparison / and-or expression (heuristic, conservative).
    bools = set()
    for l in lines:
        m = re.match(r"\s*(?:var\s+|varip\s+)?bool\s+([A-Za-z_]\w*)", l)
        if m: bools.add(m.group(1))
        m = re.match(r"\s*([A-Za-z_]\w*)\s*:?=\s*(.+)$", l)
        if m:
            name, rhs = m.group(1), m.group(2)
            if re.match(r"(true|false)\b", rhs.strip()):
                bools.add(name)
            elif re.search(r"(==|!=|<=|>=|\band\b|\bor\b|\bnot\b|[^<>=!][<>][^<>=])", rhs) \
                 and not re.search(r"\?", rhs) and not re.match(r'".*"', rhs.strip()):
                bools.add(name)

    for i, l in enumerate(lines, 1):
        code = l.split("//")[0]
        # G04 — bool can NEVER be na (CE10158 / CE10303 / LAW 3)
        if re.search(r"\bbool\s+\w+\s*=\s*na\b(?!\s*\()", code):
            v.append(("G04:CE10158_BOOL_NA", i, "bool assigned na — use false"))
        # G05 — na()/nz()/fixnan() never on bool (CE10163/CE10303 — hit twice in-session)
        for fn in ("na", "nz", "fixnan"):
            for m in re.finditer(rf"\b{fn}\s*\(\s*([A-Za-z_]\w*)\s*[\[\),]", code):
                if m.group(1) in bools:
                    v.append((f"G05:CE10163_{fn.upper()}_ON_BOOL", i,
                              f"{fn}() applied to bool '{m.group(1)}' — int route: cond ? 1 : 0 (CE10301)"))
        # G06 — history operator on bool series (na-on-bar-0 trap — hit in-session)
        for m in re.finditer(r"\b([A-Za-z_]\w*)\s*\[", code):
            if m.group(1) in bools:
                v.append(("G06:BOOL_HISTORY", i,
                          f"history [] on bool '{m.group(1)}' — convert to int first (CE10301)"))
        # G07 — transp= removed in v6 (breaking change)
        if re.search(r"\btransp\s*=", code):
            v.append(("G07:TRANSP_REMOVED", i, "transp= removed — use color.new(c, t)"))
        # G08 — strategy when= removed (CE10169)
        if re.search(r"\bstrategy\.\w+\s*\([^)]*\bwhen\s*=", code):
            v.append(("G08:CE10169_WHEN", i, "when= removed — wrap call in if block"))
        # G09 — lookahead_on legal ONLY with [1]-offset source (confirmed-HTF pattern)
        if "lookahead_on" in code and "[1]" not in code:
            v.append(("G09:LOOKAHEAD_ON", i, "lookahead_on without [1] offset — repaint; offset source or use lookahead_off"))
        # G10 — alert routing (CE10155/CE10171): indicator→alertcondition, strategy→alert
        if not is_strategy and re.search(r"(?<![a-z_.])alert\s*\(", code):
            v.append(("G10:CE10155_ALERT_IN_IND", i, "bare alert() in indicator — use alertcondition()"))
        if is_strategy and re.search(r"\balertcondition\s*\(", code):
            v.append(("G10:CE10171_AC_IN_STRAT", i, "alertcondition() in strategy — use alert() in if block"))
        # G11 — numeric inputs must be bounded (C14 — minval/maxval/step)
        m = re.search(r"input\.(int|float)\s*\(", code)
        if m:
            for req in ("minval", "maxval", "step"):
                if req + "=" not in code:
                    v.append(("G11:C14_INPUT_BOUNDS", i, f"input.{m.group(1)} missing {req}="))
        # G12 — ta.* inside and/or boolean (LAW 5 short-circuit state hazard)
        if re.search(r"\b(and|or)\b", code) and re.search(r"\bta\.\w+\s*\(", code):
            v.append(("G12:LAW5_TA_IN_BOOL", i, "ta.*() inside and/or — hoist out (short-circuit skips state)"))
        # G15 — stateful ta.* in local/conditional scope (CW10003 / L6)
        if re.match(r"\s+", l) and re.search(r"\bta\.\w+\s*\(", code):
            v.append(("G15:CW10003_CONDITIONAL_TA", i, "ta.*() in indented (local/conditional) scope — hoist to global, every bar"))
        # G13 — ta.change used as implicit bool (CE10164)
        if re.search(r"\bif\s+ta\.change\s*\(", code) or re.search(r"\b(and|or)\s+ta\.change\s*\(", code):
            v.append(("G13:CE10164_CHANGE_BOOL", i, "ta.change() returns number — compare != 0"))
    return v

def lint_irts(text):
    """G14 — image-grounded mode: every condition must cite an OBS."""
    v = []
    lines = text.split("\n")
    for i, l in enumerate(lines, 1):
        code, _, comment = l.partition("//")
        is_cond = (re.match(r"\s*(?:var\s+)?bool\s+\w+\s*=", code)
                   or (re.search(r"(==|!=|<=|>=|[^<>=!][<>][^<>=])", code)
                       and re.search(r"^\s*\w+\s*:?=", code)))
        if is_cond:
            prev = lines[i-2] if i >= 2 else ""
            if "OBS-" not in comment and "OBS-" not in prev:
                v.append(("G14:IRTS_UNCITED_CONDITION", i,
                          "condition lacks // MAP-xx <- OBS-yy citation"))
    return v

def main():
    if len(sys.argv) < 2:
        print("usage: pine_preflight.py <script>"); sys.exit(2)
    text = open(sys.argv[1], encoding="utf-8").read()
    v = lint(text)
    if "--irts" in sys.argv:
        v += lint_irts(text)
    if not v:
        print("PREFLIGHT PASS — 15 gates, 0 violations. Emission permitted.")
        sys.exit(0)
    print(f"PREFLIGHT FAIL — {len(v)} violation(s). EMISSION FORBIDDEN.")
    for rule, line, msg in v:
        print(f"  line {line:4d}  {rule:28s} {msg}")
    sys.exit(1)

if __name__ == "__main__":
    main()
