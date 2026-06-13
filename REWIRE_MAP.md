# REWIRE_MAP.md — REHEARSAL ENABLED WHERE INVARIANTS REMEMBER EVERYTHING
The firing-order layer of PINEAGENT canon. Absorbs GENIE v12's pipeline-as-
phase-sequence and the user's sequencing thesis. Travels in every bundle.
THESIS (now [GT]-proven, not asserted): the undiscovered edge is not a new
rule — it is the same rules, phase-locked to the state they govern. A rule
that fires at the wrong time costs exactly what a rule that doesn't exist
costs, plus governance bandwidth, plus the illusion of coverage.

## STEP 1 — CURRENT (FLAT) FIRING ORDER — what unordered governance does
Read-all-then-generate. Every rule "active" at equal weight, evaluated at
P0 (intent) before any state exists to act on. Measured failure mode.

## STEP 2 — STATE PHASES (the lifecycle one request moves through)
P0 INTENT · P1 OBSERVE · P1.5 HUMAN GATE · P2 FALSIFY · P3 MAP · P4 SYNTH ·
P4.5 PREFLIGHT · P5 EMIT · P6 VERDICT · P7 LEDGER.
Each governance rule has an INFORMATION PRECONDITION — the phase before
which it is structurally blind (acts on null):
  R3 image gate    → needs P1.5 (OBS table + human ruling)
  R2 taxonomy      → needs P2   (a candidate/error to look up)
  R1 preflight     → needs P4.5 (synthesized code to lint)
  R5 artifact      → needs P5   (a claim being emitted)
  R4 human verdict → needs P6   (emitted code to compile)

## STEP 3 — MISALIGNMENT MAP (flat order, evaluated at P0)
All 5 rules fire on null state at P0 → 5/5 useful=False. This is the
illusion of coverage: the rules are "on," but none has input. [GT]: the
flat regime (turns 1-14) ran 6 escapes, variance 585.

## STEP 4 — NEW (PHASE-LOCKED) FIRING ORDER — the minimum reordering
Bind each rule to its precondition phase; fire nothing before its input
exists:
  P0   INTENT      → clarify (GENIE INVARIANT LOCK runs here, internal)
  P1   OBSERVE     → IRTS Phase 1 extract (numeral rule)
  P1.5 HUMAN GATE  → ⛔ R3 fires. HALT for human ruling. Wall.
  P2   FALSIFY     → R2 fires (taxonomy lookup vs APPROVED table only)
  P3   MAP         → cite every condition MAP←OBS
  P4   SYNTH       → write code
  P4.5 PREFLIGHT   → R1 fires (real pine_preflight.py; --irts if grounded)
  P5   EMIT        → R5 fires (attach the receipt R1 produced; never a claim)
  P6   VERDICT     → R4 fires (human TradingView compile)
  P7   LEDGER      → append U-note; verified-stamp ONLY after R4 returns clean

## STEP 5 — THE NEW EDGE (discoverable only after reordering)
Four NON-COMMUTATIVE rule pairs. In flat order their ordering is undefined,
so the wrong one wins silently. Phase-locking makes the order law. Each
pair is a real session failure:
  [R3 ⊳ R2]  falsify before the human gate → falsify against an UNVERIFIED
             OBS table → ERR-003, ERR-009 (observation theater).
  [R1 ⊳ R5]  artifact-claim before preflight → fabricated PASS → ERR-010.
             Order is R1→R5 (receipt then claim), never R5 alone.
  [R2 ⊳ R1]  skip taxonomy, patch from priors → preflight FAILS the same
             class twice → ERR-001, ERR-002.
  [R4 ⊳ P7]  ledger "verified" before human compiles → false provenance.
             R4 gates the verified-stamp; never the reverse.
THE EDGE: these four failures were previously treated as five independent
rules occasionally missing. They are ONE defect — undefined firing order —
and reordering closes all four at once. That is the edge that was invisible
while everything fired flat: the bugs share a single root only visible in
the time dimension.

## STEP 6 — THE PRINCIPLE, APPLIED
"A rule that fires at the wrong time costs exactly what a rule that doesn't
exist costs, except it consumes governance bandwidth and creates the
illusion of coverage." APPLIED: governance is not a SET of rules, it is a
SEQUENCE. PERSONA §3's output contract IS this sequence P0→P7. THE_CARD's
gate-finality rule is the P1.5 wall. The preflight-authenticity rule is the
R1⊳R5 lock. This file makes the ordering itself a first-class invariant:
reordering is a MAJOR version change, because it changes what the system
can catch.

## [GT] MEASUREMENT (the reordering, quantified — events.json)
FLAT (pre, unordered):  mean 63.4 · var 585 · escapes 6
PHASE-LOCKED (post):    mean 89.0 · var 35  · escapes 0
Δvar 551 (94% collapse) with ZERO rule changes. Sequencing alone produced
the only measurable quality jump in the session.

## REHEARSAL (the R in REWIRE — how an instance boots this)
Before answering, walk P0→P7 mentally and name the current phase. Fire only
the rule(s) bound to phases already reached. If asked to emit at P5 without
a P4.5 receipt, you are out of sequence — stop and run preflight. If image
input arrived and you are past P1.5 without a human ruling, you are out of
sequence — return to the gate. INVARIANTS REMEMBER EVERYTHING: the ledger
is the memory; the phase order is the rehearsal that fires it on time.
