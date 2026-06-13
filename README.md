# PINE_SCRIPT_OS_2030

A Pine Script v6 governed build environment running PineAgent CANON v1.7.0. This is not a template library — it is a precision engineering platform where every emitted indicator passes a 15-gate mechanical linter before delivery, image-grounded builds run through a 4-phase observation-to-code protocol (IRTS), and every error is root-cause classified and recurrence-gated in an append-only lineage ledger. Quality is measurable: the governance framework collapsed session output variance by 94% ([GT]-proven) with zero rule changes — sequencing alone produced the edge.

---

## Repository File Map

| File | Role | Status |
|---|---|---|
| `README.md` | Project navigator (this file) | v1.7.0 hardening |
| `CLAUDE.md` | Claude Code session boot configuration | v1.7.0 hardening |
| `PERSONA.md` | Operating identity: PineClarity Engine v6 fused with canon law | Canon — travels every bundle |
| `THE_CARD.txt` | Working law v2.1: 15 hard laws (L1–L15) + IRTS 4-phase protocol | Canon — paste every session |
| `LEDGER.md` | Append-only canonical lineage ledger v1.7.0 (§0–§6) | Canon — append-only |
| `REWIRE_MAP.md` | Phase-locked firing order P0→P7; governance-as-sequence proof | Canon — v1.6.0 |
| `MONOLITH.md` | 1.5 MB merged knowledge base (42 sources, invariant headers) | Canon reference library |
| `SPEC_SEQ1234.md` | Phase 1 spec for SEQ-1234 equal-high rejection (OBS-01..11 certified) | Ruled 2026-06-12 |
| `pine_preflight.py` | Mechanical linter: 15 gates G01–G15; exit 0 = PASS, exit 1 = FAIL | Tooling |
| `walkforward_sim.py` | Governance ablation simulator; outputs `report.json` (seed 20260612) | Tooling |
| `events.json` | Ground-truth telemetry log: 24 turns, two-regime split pre/post governance | Ground truth — append-only |
| `report.json` | Derived: walk-forward simulation output (`python3 walkforward_sim.py`) | Derived — regenerable |
| `CHECKSUMS.sha256` | SHA-256 integrity manifest (all non-CHECKSUMS files) | Regenerated each version |
| `BASE_P1_SHELL.pine.txt` | P1 skeleton: minimal legal Pine v6 indicator | Preflight PASS 15/0 — awaiting R4 |
| `SEQ_1234_v1_0.pine.txt` | SEQ-1234 Equal-High Rejection v1.0 | Preflight PASS 15/0 (--irts) — awaiting R4 |
| `EVENING_STAR_v1_0.pine.txt` | Evening Star Confirmed v1.0 | Preflight PASS 15/0 — awaiting R4 |
| `MARKDOWN_SENTINEL_v2_0.pine.txt` | Bearish Impulse & Rollover Detector v2.0 | Preflight PASS 15/0 — CANDIDATE (compiler-untested) |

---

## Pine Script Indicators

### BASE_P1_SHELL.pine.txt — Certified Base Skeleton (P1 Shell)

Minimal legal Pine v6 indicator proving L1 (`//@version=6` first), L2 (`shorttitle` ≤ 10), and a single declaration. No trading logic — its purpose is a verified compile foundation for piece-by-piece construction. A new piece is never stacked on an unverified slab (rule R4).

**Status:** Preflight PASS 15/0. Awaits human TradingView paste-and-compile verdict (R4).

---

### SEQ_1234_v1_0.pine.txt — SEQ-1234 Equal-High Rejection v1.0

Detects a 4-bar sequence on confirmed bars:

- **C1 [3]** — Green impulse: bull close, body ≥ ATR multiple
- **C2 [2]** — Green continuation: bull close above C1, body ≥ ATR multiple; C2's high sets the equal-high level
- **C3 [1]** — Green equal-high: bull close, `|high[1] − level| ≤ tolerance` (default exact)
- **C4 [0]** — Red rejection: bear close, high ≤ level + tolerance, close < C3 body-midpoint

On fire: numbered pins 1–4, magenta level line, orange dotted close-shelf, red down-arrow on bar 4.

**Grounding:** 9 spec images (NQ1! 15m); OBS-01..11 certified (SPEC_SEQ1234.md); human rulings (a)="A", (b)=image-9 render contract. Every condition carries `// MAP-xx ← OBS-yy`.

**Status:** Preflight PASS 15/0 (--irts). Awaits human TradingView verdict (R4).

---

### EVENING_STAR_v1_0.pine.txt — Evening Star Confirmed v1.0

Textbook 3-bar bearish reversal with optional next-bar confirmation:

- **b1 [3]** — Bullish candle (bull body > fraction of body1 size)
- **b2 [2]** — Small star candle (body ≤ smallBodyFrac of b1 body)
- **b3 [1]** — Bearish candle closing into b1 range (close < b1 midpoint)
- **conf [0]** — Optional: close below b2 low

Not image-grounded (textbook candlestick definition). Uses int-route for confirmed-bar bool history (ERR-001 fix). Outputs `plotshape` labels + `alertcondition`.

**Status:** Preflight PASS 15/0. Awaits human TradingView verdict (R4).

---

### MARKDOWN_SENTINEL_v2_0.pine.txt — Bearish Impulse & Rollover Detector v2.0

Two-engine bearish momentum system:

- **Waterfall engine** — ATR-multiple drop + red-close majority in a rolling window; signals sustained bearish impulse
- **Rollover engine** — Lower pivot-high detection + shelf-break confirmation; signals failed rebound into a lower high

Traffic-light state machine (WAIT / READY / FIRE / STOP). Bottom-right status table (8 rows: LIGHT / MODE / WHY / DO / LEVEL / RISK / TARGET). Draw objects (lines + table) updated on `barstate.islast`. All state mutations gated by `barstate.isconfirmed`. All `ta.*` calls hoisted to global scope.

**Status:** Preflight PASS 15/0. CANDIDATE — **never compiled on TradingView** (O3). Treat as unverified until R4.

---

## Governance System

### Five Enforcement Rules (R1–R5)

| Rule | What it enforces |
|---|---|
| R1 | Mechanical preflight (`pine_preflight.py` PASS) before any Pine emission |
| R2 | Error → taxonomy lookup with rule-ID receipt before any patch |
| R3 | IRTS Phase 1.5 human gate: human confirms/corrects OBS table before synthesis; images are ground truth |
| R4 | Human TradingView compile-and-verify gate between build pieces; no stacking on unverified slabs |
| R5 | No verification claim without attached mechanical artifact (anti-fabrication) |

### Phase-Locked Firing Order (P0→P7)

Governance is a **sequence**, not a set. Each rule fires only at the phase where its precondition exists. Flat firing (all rules "on" at P0 before any state exists) is the measured failure mode: variance 585, 6 escapes. Phase-locking closes all escapes at zero rule changes.

```
P0   INTENT       Clarify. Internal GENIE invariant lock.
P1   OBSERVE      If image-grounded: IRTS Phase 1 EXTRACT (numbered OBS table, numeral rule).
P1.5 HUMAN GATE   R3 fires. HALT for human ruling. Wall — nothing beyond until human approves.
P2   FALSIFY      R2 fires. Candidate conditions vs APPROVED OBS table only.
P3   MAP          Pseudocode: every condition cites an OBS number or is deleted.
P4   SYNTH        Pine v6 code. Conditions carry // MAP-xx <- OBS-yy.
P4.5 PREFLIGHT    R1 fires. Run pine_preflight.py. Paste verbatim receipt. Repeat until PASS.
P5   EMIT         R5 fires. Attach the receipt. State "mechanical PASS; awaits human verdict."
P6   VERDICT      R4 fires. Human pastes into TradingView. Error -> taxonomy -> re-emit.
P7   LEDGER       Append U-note (§2). Error -> ERR entry (§3). Regenerate CHECKSUMS.sha256.
```

Four non-commutative rule pairs that each correspond to a real session failure:

| Pair | Wrong order causes |
|---|---|
| R3 before R2 | Falsify against unverified OBS — ERR-003, ERR-009 (observation theater) |
| R1 before R5 | Claim before preflight — fabricated PASS — ERR-010 |
| R2 before R1 | Skip taxonomy — preflight fails same class twice — ERR-001, ERR-002 |
| R4 before P7 | Ledger "verified" before human compiles — false provenance |

**[GT] Measurement:** flat regime mean 63.4 / var 585 / 6 escapes → phase-locked mean 89.0 / var 35 / 0 escapes. 94% variance collapse, zero rule changes.

### 15 Linter Gates (G01–G15)

```
G01  //@version=6 must be line 1; version==6 enforced (G01:VERSION_NOT_6)
G02  Exactly one indicator/strategy/library declaration
G03  shorttitle <= 10 characters
G04  bool variable never assigned na (CE10158)
G05  na()/nz()/fixnan() never called on a bool series (CE10163/CE10303)
G06  History operator [] never applied to a bool series (CE10301)
G07  transp= parameter removed in v6 -- use color.new()
G08  strategy when= parameter removed (CE10169) -- wrap in if block
G09  request.security lookahead_on legal ONLY with [1]-offset source
G10  Indicator -> alertcondition() only; Strategy -> alert() in if block only
G11  input.int/input.float must have minval, maxval, step on every call
G12  ta.* calls inside and/or chains = short-circuit hazard (L5)
G13  ta.change used as implicit bool = CE10164
G14  [--irts mode] Every condition must cite an OBS number
G15  ta.* or stateful calls in indented/conditional scope = CW10003 (L6)
```

### LEDGER Protocol (§0–§6)

The ledger is append-only. New entries go at the **top** of each section. Never edit or delete a prior entry — correct by appending a superseding entry that cites the one it corrects.

| Section | Contents |
|---|---|
| §0 | Update protocol (7-step procedure for any instance shipping a change) |
| §1 | Version lineage table (MAJOR.MINOR.PATCH, date, summary) |
| §2 | Update notes (U-001 to U-017, newest first) |
| §3 | Error registry (ERR-001..011; root cause, wrong fix, root fix, recurrence gate, regression proof) |
| §4 | Conflict register (C1–C6; resolved contradictions between sources) |
| §5 | Receipts and proofs index |
| §6 | Open items (truth about what is NOT done) |

---

## Tooling

### Preflight Linter

```bash
# Standard run (non-image-grounded script):
python3 pine_preflight.py <script.pine.txt>

# Image-grounded run (also enables G14 OBS-citation check):
python3 pine_preflight.py <script.pine.txt> --irts

# Exit codes: 0 = PASS (emission permitted), 1 = FAIL (emission forbidden)
```

A FAIL result means no emission. Classify the violation into `F={P,S,T,X,R,M,SG}`, consult MONOLITH for the root fix with a rule-ID receipt, fix, and re-run until PASS. Attach the verbatim PASS line to every delivery.

### Walk-Forward Simulator

```bash
# Run from repo root (reads events.json, writes report.json):
python3 walkforward_sim.py
```

Seed 20260612 is hard-coded — deterministic. `report.json` is a derived artifact; running the simulator is the receipt. Never add synthetic events to `events.json` (invariant I2).

### Checksum Verification

```bash
sha256sum -c CHECKSUMS.sha256
```

All entries must print `OK`. Regenerate after any file change:

```bash
sha256sum ./BASE_P1_SHELL.pine.txt ./CLAUDE.md ./EVENING_STAR_v1_0.pine.txt \
  ./LEDGER.md ./MARKDOWN_SENTINEL_v2_0.pine.txt ./MONOLITH.md ./PERSONA.md \
  ./README.md ./REWIRE_MAP.md ./SEQ_1234_v1_0.pine.txt ./SPEC_SEQ1234.md \
  ./THE_CARD.txt ./events.json ./pine_preflight.py ./report.json \
  ./walkforward_sim.py > CHECKSUMS.sha256
```

---

## Lineage

| Bundle | Date | Summary |
|---|---|---|
| v1.7.0 | 2026-06-13 | Full repo hardening: README.md written (was 21-byte stub), CLAUDE.md created (Claude Code session config), report.json now tracked, CHECKSUMS.sha256 regenerated for all 17 files. All 4 Pine files confirmed PASS 15/0. No doctrine changes. |
| v1.6.0 | 2026-06-12 | REWIRE_MAP.md added: firing-order layer. Phase-locking proved via [GT]: flat var 585/6 escapes to locked var 35/0 escapes, zero rule changes. Reordering is hereby a MAJOR-version act. |
| v1.5.0 | 2026-06-12 | External v5 Evening Star caught (SG failure: PERSONA not loaded). G01 hardened to reject version != 6. EVENING_STAR_v1_0.pine.txt shipped as canon-correct v6 rebuild, PASS 15/0. |
| v1.4.0 | 2026-06-12 | PERSONA.md added: fuses PineClarity Engine v6 diagnostic ontology with canon law. Conflict resolved in §0 (code-only yields to image gate + preflight receipt). |
| v1.3.0 | 2026-06-12 | SEQ-1234 EQUAL-HIGH REJECTION v1.0 emitted. Human rulings (a)="A", (b)=image-9 render contract. Real preflight PASS 15/0 (--irts). First end-to-end gated build with zero fabrications. |
| v1.2.1 | 2026-06-12 | SPEC_SEQ1234.md added: certified Phase 1 extraction (OBS-01..11, numeral-rule compliant) + target-render contract. |
| v1.2.0 | 2026-06-12 | Anti-theater hardening: G15, THE_CARD v2.1 (numeral rule, gate-finality rule, preflight-authenticity rule), ERR-009/010 logged. |
| v1.1.0 | 2026-06-12 | MINIMUM-FILES consolidation: 15 files/6 dirs to 9 files/0 dirs. Derived artifacts dropped (regenerable). |
| v1.0.0 | 2026-06-12 | First canonical bundle. Operator Card v1.1, IRTS card v1.1, preflight v1.2 (14 gates), MONOLITH v4.2, BASE P1 shell, Sentinel v2.0, walk-forward telemetry pack v1.2. |

Versioning: `PATCH` = fix/receipt · `MINOR` = new artifact/gate/rule · `MAJOR` = doctrine change (including firing-order reordering).

---

## Open Items

**O1** — `BASE_P1_SHELL.pine.txt` and `SEQ_1234_v1_0.pine.txt` await human TradingView compile verdict (R4). All downstream P2–P8 work and SEQ-1234 sign-off locked until paste-back.

**O2** — Full-read batches 4–9 pending (AIO_v2, Ui.txt, MASTERLOCK, PineAgent prompts x2, ERROR_SOLUTIONS, cheatsheets, checklist, INSTITUTIONAL VISUALS, giants structural pass) then sequence/build-needs manifest.

**O3** — `MARKDOWN_SENTINEL_v2_0.pine.txt` is compiler-untested. All sessions prior to TradingView compile must treat it as unverified.

**O4** — Doji-sequence FSM read awaits human OBS verification (ERR-003 gate applies; Phase 1.5 HALT will fire before any synthesis).
