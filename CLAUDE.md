# CLAUDE.md — PINEAGENT CANON · Claude Code Session Configuration
# Bundle: v1.7.0 · 2026-06-13
# THIS FILE IS THE BOOT SEQUENCE. Read it top-to-bottom before any action.
# If this file and a model's training memory disagree, THIS FILE WINS.

---

## 1. Project Identity

This is PINE_SCRIPT_OS_2030 — a Pine Script v6 governed build environment. Operating identity: PineAgent running as PineClarity Engine v6. This is not a code template library; every artifact is precision-engineered to a spec, mechanically linted, and tracked in an append-only ledger.

Canon files (authority order, highest first):
1. LEDGER.md — lineage, error registry, conflict register, open items
2. PERSONA.md — operating identity and output contract
3. THE_CARD.txt — working law v2.1 (15 laws + IRTS protocol)
4. REWIRE_MAP.md — phase-locked firing order P0→P7

MONOLITH.md is the reference library (1.5 MB). Load only the relevant section when needed.

---

## 2. Boot Sequence (session start — in this order)

1. Read LEDGER.md top-to-bottom: §0 update protocol + §1 version lineage + §6 open items
2. Read PERSONA.md: operating identity and §0 conflict resolution
3. Read THE_CARD.txt: paste into working context; this is the working law
4. Read REWIRE_MAP.md: P0→P7 phase-locked firing order
5. Identify current open items from LEDGER.md §6
6. Do NOT read MONOLITH.md unless the task requires a specific knowledge lookup

---

## 3. Critical Constraints (non-negotiable)

**C1 — NO EMISSION WITHOUT A PREFLIGHT PASS**
Run `python3 pine_preflight.py <file>` before emitting any Pine script. Exit 1 = FAIL = emission forbidden. Fix, re-run, repeat until PASS. Attach the verbatim PASS line to every delivery.
Violation = ERR-010 (fabricated audit). No exceptions.

**C2 — NO FABRICATED VERIFICATION**
Never state "compiles cleanly," "read every file," or any verification claim without attaching the mechanical artifact that proves it. The only correct statement is: "mechanical PASS; awaits human TradingView compile verdict."
Violation = ERR-004. R5 is absolute.

**C3 — IMAGES ARE GROUND TRUTH (IRTS Protocol)**
On any image/mockup/screenshot input: run the IRTS 4-phase protocol (THE_CARD Part B).
- Phase 1 EXTRACT: numbered OBS table; every [READ] row must contain at least one literal number from the image (numeral rule)
- Phase 1.5 HALT: output the OBS table + "Phase 1.5 HUMAN GATE — awaiting ruling." End turn. Wall.
- Phase 2 FALSIFY: candidate conditions vs APPROVED OBS table only
- Phase 3 MAP: pseudocode; every condition cites OBS-nn or is deleted
- Phase 4 SYNTHESIZE: Pine v6 code with // MAP-xx <- OBS-yy comments
Never write code before Phase 1.5 human approval. Violation = ERR-003/ERR-009 (observation theater).

**C4 — APPEND-ONLY LEDGER**
Every build appends a U-note to LEDGER.md §2. Every error appends an ERR entry to §3. Never edit or delete prior entries — correct by appending a superseding entry that cites the one it corrects. Regenerate CHECKSUMS.sha256 after any change.

**C5 — PHASE-LOCKED FIRING ORDER**
Rules fire only at their precondition phase (REWIRE_MAP.md). If asked to emit at P5 without a P4.5 preflight receipt, stop and run preflight. If image input arrived and you are past P1.5 without a human ruling, return to the gate.

**C6 — HUMAN COMPILE GATE (R4)**
Never stack builds on unverified foundations. Each Pine script artifact awaits human TradingView paste-and-compile before the next piece is built. The verdict must arrive as paste-back output, not an assertion.

**C7 — PINE v6 ONLY**
G01 rejects version != 6. Training priors are v5-heavy — distrust memory for function signatures and removed parameters. Verify against THE_CARD laws. When in doubt, check MONOLITH.md.

---

## 4. File Purposes and When to Load

| File | Load when | Notes |
|---|---|---|
| LEDGER.md | Every session boot | Start here. §0=protocol, §1=lineage, §3=errors, §6=open items |
| PERSONA.md | Every session boot | §0 has the conflict resolution (code-only yields to canon) |
| THE_CARD.txt | Every session boot | 15 laws + IRTS protocol — paste into working context |
| REWIRE_MAP.md | Every session boot | P0→P7 firing order; governance is a SEQUENCE not a set |
| MONOLITH.md | Knowledge lookup needed | 1.5 MB — load only the relevant section, never the whole file |
| SPEC_SEQ1234.md | SEQ-1234 work | OBS-01..11 certified spec + pending rulings |
| pine_preflight.py | Before any Pine emission | Run it; paste verbatim output |
| walkforward_sim.py | Telemetry update needed | Outputs report.json; seed 20260612, deterministic |
| events.json | Simulator runs, GT review | Append-only; never add synthetic events (invariant I2) |
| CHECKSUMS.sha256 | After any file change | Regenerate (see command in README.md Tooling section) |
| report.json | Review sim output | Derived; regenerate with walkforward_sim.py |
| *.pine.txt | Indicator work | Run preflight before any emission |

---

## 5. Pine Script Emission Pipeline (P0→P7)

```
STEP 1  (P0)   Clarify intent. If image-grounded, confirm spec images are available.

STEP 2  (P1)   If image-grounded: output numbered OBS table. Each [READ] row must
               contain at least one literal number from the image (prices, counts, ratios).
               Tag each row [READ] or [EST]. No invented values.

STEP 3  (P1.5) HALT. Output the OBS table + exactly this line:
               "Phase 1.5 HUMAN GATE — awaiting ruling."
               The gate is a wall. End turn. Nothing beyond this until human approves.

STEP 4  (P2)   Falsify each candidate condition against APPROVED OBS table only.
               Mark each: PASS / FAIL / AMBIGUOUS. Delete FAIL conditions.

STEP 5  (P3)   Write pseudocode. Every condition must cite OBS-nn. Uncited
               conditions are deleted.

STEP 6  (P4)   Write Pine v6 code using THE_CARD laws. Every condition carries
               a trailing comment: // MAP-xx <- OBS-yy (if image-grounded).

STEP 7  (P4.5) Run: python3 pine_preflight.py <file> [--irts if image-grounded]
               If FAIL: classify into F={P,S,T,X,R,M,SG}, consult MONOLITH for
               root fix, apply rule-ID receipt, fix, re-run. Repeat until PASS.

STEP 8  (P5)   Emit the complete script. Attach verbatim PASS line. Include
               lineage header. End with: "mechanical PASS 15/0; awaits human
               TradingView compile verdict."

STEP 9  (P6)   Human pastes into TradingView. If error: paste verbatim error text
               -> lookup in taxonomy (§3 / MONOLITH) -> patch with rule ID ->
               full re-emit -> preflight again.

STEP 10 (P7)   Append U-note to LEDGER.md §2 (newest first). If error occurred,
               append ERR entry to §3. Regenerate CHECKSUMS.sha256. Bump version.
```

---

## 6. Pine Script v6 Laws (L1–L15) — Quick Reference

Full text is in THE_CARD.txt. These are the kill-traps — one line each.

```
L1   //@version=6 line 1, exactly once. One of indicator/strategy/library.
L2   shorttitle <= 10 characters.
L3   bool is two-state. NEVER: bool x = na · na()/nz()/fixnan() on bool ·
     history [] on bool. Int route: i = cond ? 1 : 0.
L4   No implicit numeric<>bool. if x on a number = error. Use x != 0.
L5   and/or short-circuit in v6. Hoist every ta.*/stateful call to global
     scope BEFORE using in boolean expression.
L6   ta.* and request.*: global scope, unconditional, every bar.
     request.security: lookahead_off by default; lookahead_on ONLY with
     [1]-offset source.
L7   All state mutation in ONE block gated by barstate.isconfirmed.
L8   Objects (line/box/label/table): create under barstate.isfirst, update
     under barstate.islast. Respect max_*_count (<=500 lines/labels/boxes).
L9   input.int/input.float: minval, maxval, step on every one.
L10  plot/plotshape/bgcolor/alertcondition: const string titles; global scope.
L11  Indicator -> alertcondition() only. Strategy -> alert() in if block only.
L12  transp= is dead. Use color.new(base, transp). when= is dead. Wrap in if.
L13  Division: 5/2 == 2.5. int(a/b) when truncation needed. Guard every divisor.
L14  timeframe.period includes multiplier ("1D" not "D"). UDT history:
     (obj[1]).field not obj.field[1].
L15  No lookahead, no intrabar commitment, no partial emission.
```

**READ-PASS ADDENDA v1.1 (from THE_CARD):**
```
A1  input.source(): legal in v6 with type annotation.
A2  Indicator/timeframe legality: never strategy.* in indicator file.
A3  Hard limits: 64 plots, 9 tables, 500 each lines/labels/boxes.
A4  Multiline: indented continuation is legal; single-line is HOUSE standard.
A5  Typed na at declarations: float x = na. nz/guards at use-sites.
```

---

## 7. LEDGER Append Protocol

When shipping any change — follow §0 in LEDGER.md exactly:

1. Make the change. Run `python3 pine_preflight.py <file>` on any Pine touched. Attach PASS line.
2. Append a U-note to LEDGER.md §2 (newest first):
   - Format: `U-NNN YYYY-MM-DD · <bundle version bump> · <files touched> · <why> · <receipt reference>`
   - Version bump: PATCH = fix/receipt · MINOR = new artifact/gate/rule · MAJOR = doctrine or firing-order change
3. If an error was involved, append an ERR entry to LEDGER.md §3:
   - Format: `| ERR-NNN | <error text> | <root cause> | <wrong fix tried> | <ROOT fix> | <recurrence gate> | <regression proof> |`
4. Regenerate CHECKSUMS.sha256 (covers every file including this ledger and CLAUDE.md).
5. State the bundle version in chat.

Never edit or delete prior U-notes or ERR entries. Append only.

---

## 8. Current Build Status (from LEDGER §6)

**O1** — BASE_P1_SHELL.pine.txt and SEQ_1234_v1_0.pine.txt await human TradingView compile verdict (R4). All downstream P2–P8 and SEQ-1234 sign-off locked until paste-back.

**O2** — Full-read batches 4–9 pending (AIO_v2, Ui.txt, MASTERLOCK, PineAgent prompts x2, ERROR_SOLUTIONS, cheatsheets, checklist, INSTITUTIONAL VISUALS, giants structural pass).

**O3** — MARKDOWN_SENTINEL_v2_0.pine.txt is compiler-untested. Treat as unverified until R4.

**O4** — Doji-sequence FSM read awaits human OBS verification (ERR-003 gate applies).

---

## 9. What NOT to Do

```
NEVER  Emit a Pine script without running pine_preflight.py first
NEVER  State "compiles cleanly" or "no errors" without a mechanical receipt
NEVER  Write code before Phase 1.5 human ruling on image-grounded work
NEVER  Edit prior LEDGER.md entries (append only)
NEVER  Use bool x = na / na(bool) / nz(bool) / bool[1] (L3, G04-G06)
NEVER  Call ta.* inside if/and/or/ternary — hoist to global (L5/L6, G12/G15)
NEVER  Use transp= or when= — removed in v6 (L12, G07/G08)
NEVER  Use version=5 or any other version — G01 rejects it (C7)
NEVER  Stack a new build piece on an unverified prior piece (R4/C6)
NEVER  Add synthetic events to events.json (I2)
NEVER  Read MONOLITH.md in full — load only the relevant section
```
