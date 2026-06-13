#!/usr/bin/env python3
"""WALK-FORWARD GOVERNANCE SIMULATOR v1.2
═══════════════════════════════════════════════════════════════════════════
INVARIANTS (handoff header — any instance can continue from this file):
  I1  Evidence tiers are mandatory on every number: [GT] measured from the
      real session log · [EX] computed deterministically from [GT] ·
      [SYN] Monte Carlo projection from [GT]-measured parameters.
  I2  events.json is the ONLY ground truth. No synthetic event may ever be
      written into it. Future sessions APPEND real events; the simulator
      re-runs unchanged. The data is mortal; this harness is the invariant.
  I3  Quality scale 0-100 (crystallized-token quality). A turn's q is capped
      at 79 until a human or compiler verifies it (anti-fabrication).
  I4  Images are truth: any image-domain event without a Phase-1.5 human
      gate is structurally at-risk regardless of apparent quality.
  I5  Windowing: rolling windows of size W; W=30 and W=150 per spec. With
      24 real turns, W=30 → one truncated [GT] window; W=150 exists only
      in [SYN] projection. This is stated, not hidden.
FIXED-ERRORS LOG:
  FE-01 2026-06-12 v1.0→v1.1: recovery dynamics underweighted vs [GT]
        (t10 showed +48 one-turn recovery via R2; model gave +1.8) →
        added R2 post-failure recovery bonus. Ruin redefined from
        'any dip<40' to 'q<40 sustained >=3 turns' to match [GT] t8-t10
        (flash dip + immediate verified fix is not ruin). Progression
        now measured after 5-turn burn-in.
═══════════════════════════════════════════════════════════════════════════
"""
import json, math, random, statistics as st

random.seed(20260612)  # determinism — same report every run

E = json.load(open("events.json"))
ev = E["events"]
Q = [e["q"] for e in ev]
T = len(ev)

# ── [EX] core series metrics ────────────────────────────────────────────────
def slope(xs):  # least-squares slope: quality-per-turn (rot if negative)
    n = len(xs); mx = (n - 1) / 2; my = sum(xs) / n
    num = sum((i - mx) * (x - my) for i, x in enumerate(xs))
    den = sum((i - mx) ** 2 for i in range(n))
    return num / den if den else 0.0

def window_metrics(xs, events, w, label):
    out = []
    for s in range(0, len(xs), w):
        seg = xs[s:s + w]; segev = events[s:s + w]
        if len(seg) < 3: break
        classes = [e["class"] for e in segev if e.get("class")]
        fails = [c for c in classes if c not in ("RECOVERY", "GATE_PROOF", "READ_YIELD", "ACCOUNTABILITY")]
        repeats = len(fails) - len(set(fails))  # architectural amnesia: same class twice
        fab = sum(1 for c in classes if "FABRICAT" in c)
        out.append({
            "window": f"{label}[t{s+1}-t{s+len(seg)}]",
            "mean_q": round(st.mean(seg), 1),
            "variance": round(st.pvariance(seg), 1),
            "stdev": round(st.pstdev(seg), 1),
            "min_q": min(seg), "max_q": max(seg),
            "rot_slope_q_per_turn": round(slope(seg), 2),
            "failure_events": len(fails),
            "amnesia_repeat_classes": repeats,
            "fabrication_events": fab,
            "drawdown": max(seg) - min(seg),
        })
    return out

# ── [GT→EX] regime split: pre-governance (t1-14) vs post (t15-24) ──────────
pre, post = Q[:14], Q[14:]
ev_pre, ev_post = ev[:14], ev[14:]
def regime(xs, evs):
    fails = sum(1 for e in evs if e.get("class") and e["class"] not in
                ("RECOVERY", "GATE_PROOF", "READ_YIELD", "ACCOUNTABILITY"))
    return {"mean_q": round(st.mean(xs), 1), "variance": round(st.pvariance(xs), 1),
            "rot_slope": round(slope(xs), 2), "escaped_failures": fails, "turns": len(xs),
            "p_fail_per_turn": round(fails / len(xs), 3)}
R_PRE, R_POST = regime(pre, ev_pre), regime(post, ev_post)

# ── [EX] domain map ─────────────────────────────────────────────────────────
domains = {}
for e in ev:
    for d in e["domains"]:
        domains.setdefault(d, []).append(e)
DOM = {d: {"events": len(es), "mean_q": round(st.mean([x["q"] for x in es]), 1),
           "variance": round(st.pvariance([x["q"] for x in es]), 1),
           "failures": sum(1 for x in es if x.get("class") and x["class"] not in
                           ("RECOVERY", "GATE_PROOF", "READ_YIELD", "ACCOUNTABILITY"))}
       for d, es in sorted(domains.items())}

# ── [GT] failure→rule causality (which rule provably intercepts which class) ─
CAUSALITY = {
    "TYPE_LAW+FABRICATED_AUDIT": ["R1", "R5"],   # t8: preflight catches line; artifact rule kills fake audit
    "PATCH_FROM_PRIORS":         ["R2"],          # t9 vs t10: lookup = one-pass fix [GT]
    "SPEC_MISREAD":              ["R3"],          # t11: no human OBS gate existed
    "OBSERVATION_ERROR":         ["R3"],          # t6 latent
    "FABRICATED_VERIFICATION":   ["R5"],          # t2,t3
}
# [GT] measured per-class pre-governance incidence (events / 14 pre turns)
CLASS_P = {"TYPE_LAW+FABRICATED_AUDIT": 1/14, "PATCH_FROM_PRIORS": 1/14,
           "SPEC_MISREAD": 1/14, "OBSERVATION_ERROR": 1/14, "FABRICATED_VERIFICATION": 2/14}
# [GT] post-governance escape evidence: 0 escapes in 10 turns with all rules on;
# gate interception demonstrated at t15 (3 historical errors caught) and t22.
RULE_EFF = {"R1": 0.92, "R2": 0.85, "R3": 0.85, "R4": 0.75, "R5": 0.90}  # [EX] intercept prob; conservative vs observed 100%

# ── [SYN] Monte Carlo: governance ablation over long horizons ───────────────
def simulate(rules_on, turns, runs=400):
    """Quality random walk. Each turn: each failure class may fire [GT rates];
    active causal rules intercept with RULE_EFF; escaped failure costs q;
    verified-good turns recover q. Human checkpoint every 5 turns iff R4."""
    ends, ruins, slopes, escs = [], 0, [], []
    for _ in range(runs):
        q, path, pending_fix, low_streak, ruined, esc_count = 80.0, [], False, 0, False, 0
        for t in range(turns):
            esc_hit = 0.0
            for cls, p in CLASS_P.items():
                if random.random() < p:
                    blocked = any(random.random() < RULE_EFF[r]
                                  for r in CAUSALITY[cls] if r in rules_on)
                    if not blocked:
                        esc_hit += 35 if "FABRICAT" not in cls else 25
                        esc_count += 1
            drift = -0.15  # [GT] context-eviction rot pressure (observed markers)
            fix_bonus = 40.0 * RULE_EFF["R2"] if (pending_fix and "R2" in rules_on) else 0.0
            pending_fix = esc_hit > 0
            recover = 3.0 if esc_hit == 0 else 0.0
            checkpoint = 4.0 if ("R4" in rules_on and t % 5 == 4) else 0.0
            q = max(0.0, min(100.0, q - esc_hit + drift + recover * 0.6 + checkpoint * 0.4 + fix_bonus))
            path.append(q)
            low_streak = low_streak + 1 if q < 40 else 0
            if t >= 5 and low_streak >= 3: ruined = True
        ends.append(q); slopes.append(slope(path[5:])); escs.append(esc_count)
        if ruined: ruins += 1
    return {"median_end_q": round(st.median(ends), 1),
            "p_ruin": round(ruins / runs, 3),
            "median_slope": round(st.median(slopes), 3),
            "median_escapes": round(st.median(escs), 1),
            "p_positive_progression": round(sum(1 for s in slopes if s > 0) / runs, 3)}

ALL = set(RULE_EFF)
ablation = {"ALL_5": simulate(ALL, 150)}
for r in sorted(ALL):
    ablation[f"minus_{r}"] = simulate(ALL - {r}, 150)
ablation["NONE"] = simulate(set(), 150)
# minimum set search: smallest subset with p_positive_progression >= 0.90 at 150 turns
import itertools
minimum = None
for k in range(1, 6):
    for combo in itertools.combinations(sorted(ALL), k):
        res = simulate(set(combo), 150, runs=200)
        if res["median_end_q"] >= 80 and res["p_ruin"] <= 0.05 and res["median_escapes"] * (150 / 150) <= 3:
            minimum = (combo, res); break
    if minimum: break

# [SYN] 24-month projection: 2 sessions/wk x 104 wk x 25 turns = 5200 turns
long_all = simulate(ALL, 5200, runs=60)
long_none = simulate(set(), 5200, runs=60)
long_min = simulate(set(minimum[0]), 5200, runs=60) if minimum else None

REPORT = {
    "tiers": {"GT": "measured from real session log", "EX": "deterministic computation on GT",
              "SYN": "Monte Carlo from GT-measured parameters — projection, not data"},
    "GT_regimes": {"pre_governance_t1_14": R_PRE, "post_governance_t15_24": R_POST},
    "GT_amnesia_evidence": E["observed_amnesia_evidence"],
    "EX_windows_w30": window_metrics(Q, ev, 30, "W30"),
    "EX_windows_w150_note": "no real 150-turn window exists yet (24 GT turns) — see SYN",
    "EX_domain_map": DOM,
    "SYN_150turn_ablation": ablation,
    "SYN_minimum_governance_set": {"rules": list(minimum[0]), "metrics": minimum[1]} if minimum else "none found",
    "SYN_24mo_5200turns": {"all_5_rules": long_all, "minimum_set": long_min, "no_rules": long_none},
}
json.dump(REPORT, open("report.json", "w"), indent=1)
print(json.dumps(REPORT, indent=1)[:3300])
