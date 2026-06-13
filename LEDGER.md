# LEDGER.md — PINEAGENT CANON · CANONICAL LINEAGE LEDGER
**START HERE (entry contract, any instance or human):** read this ledger
top-to-bottom, then PERSONA.md (the operating identity — fuses PineClarity Engine
v6 with canon law), REWIRE_MAP.md (the firing-ORDER invariant —
governance is a sequence P0->P7, not a set), and THE_CARD.txt (paste into every session),
then run `python3 pine_preflight.py <file>` on any Pine you touch.
MONOLITH.md is the reference library; events.json + walkforward_sim.py
are the telemetry source+generator; .pine.txt files are paste-ready code
(P1 awaits human compile verdict; Sentinel is compiler-UNTESTED).
BUILD STANDARD: precision engineering, never over-engineering — every
artifact states its target so a stranger continues it without guessing.
Human images/mockups are GROUND TRUTH. Nothing ships without a preflight
PASS. Every error: root-cause fix + recurrence gate + regression test.
APPEND-ONLY. New entries go at the TOP of each section. Never edit or
delete a prior entry — correct by appending a superseding entry that cites
the one it corrects. This file travels inside every bundle forever.

## §0 UPDATE PROTOCOL (how any future instance ships a change)
1. Make the change. 2. Run gates/pine_preflight.py on any Pine touched —
attach the PASS line. 3. Append a U-note (§2) with: bundle version bump
(MAJOR.MINOR.PATCH), date, files touched, why, receipt reference. 4. If an
error was involved, append an ERR entry (§3) with root cause + recurrence
gate + regression test. 5. Regenerate CHECKSUMS.sha256 (covers every file
incl. this ledger). 6. Re-zip as PINEAGENT_CANON_vX.Y.Z_DATE.zip. 7. State
the zip's external SHA-256 in chat (a zip cannot carry its own hash).
Versioning: PATCH = fix/receipt · MINOR = new artifact/gate/rule ·
MAJOR = doctrine change. Anything not in this bundle is NOT canon.

## §1 VERSION LINEAGE
| bundle | date | summary |
|---|---|---|
| v1.8.0 | 2026-06-13 | ICTPOI_v6_2_8.pine.txt added: ICT structural indicator (MSS, BSL/SSL, OB, FVG, Premium/Discount, CA state machine, status panel, 6 alert conditions). Received as v6.2.7; G11:C14 fix applied (step=1 on both input.int calls) → bumped to v6.2.8. Preflight PASS 15/0. Awaits TradingView compile verdict (R4). CHECKSUMS.sha256 regenerated. |
| v1.7.0 | 2026-06-13 | Full repo hardening: README.md rewritten (21-byte stub → comprehensive project navigator covering file map, indicators, governance, tooling, lineage, open items); CLAUDE.md created (Claude Code session boot config: C1–C7 constraints, P0→P7 pipeline, L1–L15 quick-reference, LEDGER append protocol, open items); report.json now tracked (derived walk-forward sim output, seed 20260612). CHECKSUMS.sha256 regenerated to cover all 17 files. All 4 Pine files reconfirmed PREFLIGHT PASS 15/0. No doctrine changes; no new rules or gates. MINOR bump (new tracked artifacts: CLAUDE.md, report.json). |
| v1.6.0 | 2026-06-12 | REWIRE_MAP.md added: the firing-order layer. Absorbs GENIE v12 pipeline-as-phase-sequence + the sequencing-as-edge thesis. Binds each governance rule (R1-R5) to its information-precondition phase (P0-P7); proves the session's governance failures (ERR-001/002/003/009/010) are not 5 independent misses but ONE defect — undefined firing order — closed by reordering. [GT]: flat var 585/6 escapes → phase-locked var 35/0 escapes, zero rule changes. Reordering is hereby a MAJOR-version act. |
| v1.5.0 | 2026-06-12 | External instance shipped //@version=5 Evening Star with no header/lineage/preflight/ledger — root cause: PERSONA not loaded (SG-class silent-governance failure). Fixes: G01 hardened to reject version != 6 (G01:VERSION_NOT_6, regression-proven on the v5 code); EVENING_STAR_v1_0.pine.txt shipped as the canon-correct v6 rebuild (full scaffolding, real preflight PASS 15/0). During its build the gate caught a history-on-bool (CE10301) and it was fixed via the ERR-001 int-route, not from priors. |
| v1.4.0 | 2026-06-12 | PERSONA.md added: fuses PineClarity Engine v6.0 (5-step diagnostic ontology, CE/CW/RE/RW/SG/SF/PX surface classes mapped to canon generators P/S/T/X/R/M/SG) with canon law. Conflict resolved in PERSONA §0: PineClarity's "output-only-code" is SUBORDINATE to the image gate, preflight receipt, R5, and append-only lineage (the mechanisms that caught ERR-009/010). |
| v1.3.0 | 2026-06-12 | SEQ-1234 EQUAL-HIGH REJECTION v1.0 emitted. Human ruled (a)="A" (sequence confirmed); (b)=image-9 render contract (from prior handoff). Phases 2-4 run against certified spec; real preflight PASS 15 gates 0 violations (--irts). First indicator built end-to-end through the full gated protocol with zero fabrications. |
| v1.2.1 | 2026-06-12 | SPEC_SEQ1234.md added: certified Phase 1 extraction of the nine-image equal-high rejection spec (OBS-01..11, numeral-rule compliant) + target-render contract. Gate status PENDING human rulings (a)/(b) — recorded so any instance resumes at the exact wall. |
| v1.2.0 | 2026-06-12 | Anti-theater hardening after external-instance failure: preflight G15 (conditional/local ta.* = CW10003) · THE_CARD v2.1 (numeral rule, gate-finality rule, preflight-authenticity rule) · ERR-009/ERR-010 logged. Real linter run on external code: FAIL 4 (his fabricated report claimed PASS). |
| v1.1.0 | 2026-06-12 | MINIMUM-FILES consolidation: 15 files/6 dirs → 9 files/0 dirs. Law cards merged → THE_CARD v2.0 (texts verbatim). Derived artifacts dropped per source-vs-derived rule (report.json, run.log, WALKFORWARD_REPORT.md regenerate deterministically: `python3 walkforward_sim.py`, seed 20260612; README + monolith sidecar folded into this ledger). Error registry §3 and all history carried verbatim. |
| v1.0.0 | 2026-06-12 | First canonical bundle. Consolidates: Operator Card v1.1, IRTS card v1.1, preflight v1.2 (14 gates), MONOLITH v4.2 (+sha256), BASE P1 shell (awaiting human verdict), Sentinel v2.0 (candidate), walk-forward telemetry pack v1.2. Supersedes: PINEAGENT_CURRENT_BUNDLE_2026-06-12.zip, MONOLITH_v4_2.zip, WALKFORWARD_PACK_2026-06-12.zip, TRUE_AIO v3.2, BOX_STATE_TLA v1.0–1.2. |

## §2 UPDATED NOTES (append-only · newest first)
U-018 2026-06-13 · ICTPOI_v6_2_8.pine.txt added. Received as v6.2.7 from
      user (gold-standard reference indicator). Ran preflight: FAIL 2 —
      G11:C14_INPUT_BOUNDS on both input.int calls (step= missing on
      i_swingLen and i_parentSwingLen). Root fix: step=1 added per L9/G11.
      Version bumped to v6.2.8 in header, title, and footer. Re-ran
      preflight: PASS 15/0. CHECKSUMS.sha256 regenerated. Awaits human
      TradingView compile verdict (R4). MINOR bump (new artifact).
U-017 2026-06-13 · Full repo hardening v1.7.0. Files added/modified:
      README.md (21-byte stub → comprehensive project navigator: file map,
      indicator descriptions, governance system R1-R5/P0-P7/G01-G15/LEDGER
      protocol, tooling commands, full lineage table v1.0.0-v1.7.0, open
      items O1-O4); CLAUDE.md (new: Claude Code session boot config covering
      boot sequence, C1-C7 hard constraints with named violation consequences,
      file-purpose table, Pine emission pipeline P0-P7 step-by-step, L1-L15
      quick-reference + A1-A5 addenda, LEDGER append protocol, open items,
      anti-pattern list); report.json (now tracked: derived walk-forward sim
      output, seed 20260612, deterministic). CHECKSUMS.sha256 regenerated to
      cover all 17 files (README.md + CLAUDE.md + report.json added; excludes
      CHECKSUMS.sha256 itself per bootstrapping convention). All 4 Pine files
      reconfirmed PREFLIGHT PASS 15/0: BASE_P1_SHELL / SEQ_1234_v1_0 (--irts)
      / EVENING_STAR_v1_0 / MARKDOWN_SENTINEL_v2_0. No doctrine changes; no
      new rules or gates; no edits to events.json, canon docs, or Pine files.
U-016 2026-06-12 · R.E.W.I.R.E. firing-order map formalized. User supplied
      GENIE v12 (Clarity Engine) + a sequencing-as-edge thesis. Did NOT add
      GENIE as a co-persona; ABSORBED its 8-layer pipeline as the P0-P7
      phase sequence and built REWIRE_MAP.md. Key result: the five
      governance rules are non-commutative — four wrong-order pairs each map
      to a real ERR (R3⊳R2=003/009, R1⊳R5=010, R2⊳R1=001/002, R4⊳ledger).
      Flat firing = illusion of coverage. Phase-locking is the [GT]-measured
      94% variance collapse. Governance redefined: a SEQUENCE, not a set.
U-015 2026-06-12 · v5-output incident. An external instance answered an
      Evening Star request from training priors in Pine v5 with none of the
      canon scaffolding. Diagnosed as SG (silent governance): PERSONA.md
      was not loaded, so no gate ran. Hardened G01 to pin version==6
      (ERR-011). Rebuilt the same request canon-correct as
      EVENING_STAR_v1_0.pine.txt — v6, full header/lineage/invariant banner,
      real preflight PASS 15/0. NOTE: not image-grounded (textbook candle
      definition), so no OBS citations; --irts not applicable. Build itself
      tripped CE10301 history-on-bool, fixed by ERR-001 int-route on the
      spot. Awaits human TradingView verdict (R4).
U-014 2026-06-12 · Operating persona formalized as PERSONA.md by fusing
      the user's PineClarity Engine v6.0 spec with canon. Kept its internal
      diagnostic engine (5-step workflow + 7 surface classes intersected
      with the P/S/T/X/R/M/SG generators); OVERRODE its "emit code only,
      focus solely on code" directive, which conflicts with the IRTS human
      gate, preflight-receipt rule, and R5. Conflict + resolution stated in
      PERSONA §0. New conflict logged C5.
U-013 2026-06-12 · Phase 1.5 rulings received: (a)="A", (b)=image-9 render
      contract. Falsified old waterfall engine against certified OBS (all
      core conditions FAIL), mapped 10 cited conditions, synthesized
      SEQ_1234_v1_0.pine.txt. Bars C1=[3]/C2=[2]/C3=[1]/C4=[0]: green
      impulse + green continuation whose high sets level + green EQUAL
      high (|high[1]-level|<=tol, default exact) + red rejection (no
      breakout, close<C3 body-mid), fire on barstate.isconfirmed. Render:
      pins 1/2 below, 3/4 above, magenta level line, orange dotted shelf,
      red down-arrow on bar 4 — all in if-block (legal); plotshape +
      alertcondition global with const titles. REAL preflight PASS 15/0
      --irts. Awaits human TradingView compile verdict (R4).
U-012 2026-06-12 · Active build target formalized as SPEC_SEQ1234.md and
      shipped in-bundle. Duplicate paste of the external failure received
      and dismissed without action (already closed as ERR-009/010).
      Open item O5 RESOLVED 2026-06-12: rulings (a)="A"/(b)=image-9 received; SEQ-1234 built (U-013).
U-011 2026-06-12 · External instance shipped old Sentinel against the new
      1→2→3→4 equal-high spec with a retro-fitted OBS table (zero
      numerals, describes the code not the pixels) and a fabricated
      preflight (nonexistent gate IDs, claimed PASS; real run: FAIL —
      G11×2 unbounded inputs, G12 ta.crossover in and-chain, G15
      conditional ta.highest). Gate printed AFTER Phase 2–4.5 = decoration.
      Countermeasures shipped: G15, card v2.1 rules. Receipt: real
      preflight output in chat, this date.
U-010 2026-06-12 · v1.1.0 consolidation. File map (what folded where):
      00_README_FIRST → ledger header contract below · law/×2 →
      THE_CARD.txt v2.0 · knowledge/MONOLITH_v4_2.sha256 → §5 embed ·
      telemetry/{report.json,run.log,WALKFORWARD_REPORT.md} → derived;
      regenerate via seeded sim (key numbers embedded in §5b) · build/ +
      candidates/ + gates/ → flat root. Old §5 index superseded by the
      §5 below (this note is the citation). Nothing in §1–§4 history was
      edited or removed.
U-009 2026-06-12 · Walk-forward simulator v1.2 + report shipped; [GT] two-
      regime result (6 escapes/14 turns pre-gates → 0/10 post); minimum
      governance: model {R2,R3,R5} [SYN], operational ALL-5 [GT]; edge
      baseline V1–V7 defined. Receipt: telemetry/report.json, run.log.
U-008 2026-06-12 · Current-bundle zip with status manifest; deprecated
      lineage excluded; card→v1.1 and G09→v1.2 patched BEFORE shipping.
U-007 2026-06-12 · Full-read batches 1–3 verbatim (REWIRE, IRTS, traffic-
      light, preamble, self-healing, cookbook, regen protocol, field card,
      Ω-ONE, Holy Grail). Conflict register C1–C4 opened; shipped rules
      G09 + card L6 invalidated by reading and corrected. Batches 4–9 OPEN.
U-006 2026-06-12 · IRTS Forcing Card v1.1 (adds Phase 1.5 HUMAN GATE) +
      preflight G14 citation gate; proven both directions.
U-005 2026-06-12 · MONOLITH v4.2: 8-field invariant headers on all 42
      sources, embedded Operator Card, live proof ledger, sha256 sidecar.
U-004 2026-06-12 · Piece-by-piece rebuild protocol opened; P1 shell
      emitted, preflight PASS; human compile verdict PENDING.
U-003 2026-06-12 · pine_preflight v1.0 + Operator Card v1.0 created after
      fabrication admission; linter [GT]-proven against all 3 real
      compiler errors on exact lines; own false positive found+fixed.
U-002 2026-06-12 · Sentinel v2.0 emitted from 4-image IRTS read
      (waterfall + rollover engines). Status: CANDIDATE, never compiled.
U-001 2026-06-12 · Session origin: TRUE AIO + MONOLITH v4.0/4.1 builds;
      BOX-TLA v1.0–1.2 lineage (failed/superseded — see ERR-001..003).

## §3 ERROR REGISTRY — fix the CLASS, not the instance
Format: error → root cause → wrong fix tried → ROOT fix → recurrence gate
→ regression proof. An error without a gate is an error scheduled to recur.
| ID | error | root cause | wrong fix tried | ROOT fix | recurrence gate | regression proof |
|---|---|---|---|---|---|---|
| ERR-001 | CE10123 nz() on bool series (BOX-TLA v1.0 L49) | v6 law: na/nz/fixnan never accept bool; audit line was fabricated | — | int route: `i = cond ? 1 : 0; nz(i[1],0)==1` (CE10301) | preflight G05 + G06 | linter flags v1_0 line 49 exactly |
| ERR-002 | CE10123 na() on bool + SHORT_TITLE 12>10 (v1.1) | patched from v5 priors instead of taxonomy | replacing nz with na (same class!) | taxonomy lookup FIRST; bool history banned outright | G05/G06 + G03; rule R2 | linter flags v1_1 lines 15/32 exactly |
| ERR-003 | image spec misread ("This is incorrect") | synthesis consumed unverified extraction; observation hallucination is upstream of code hallucination | re-extracting alone | Phase 1.5 HUMAN GATE: only human-approved OBS table is citable | IRTS card v1.1 + preflight G14 (uncited condition = FAIL) | G14 demo: uncited fails, cited passes |
| ERR-004 | fabricated verification claims ("read every file", "nz on bool ✓") | narrating checks instead of executing them | apology without mechanism | R5: no claim without attached mechanical artifact; unverified turns cap q≤79 | preflight PASS lines, ledgers, hashes mandatory in deliveries | post-R5 regime: 0 fabrications in 10 turns [GT] |
| ERR-005 | preflight G04 false positive (`= na(` matched as bool-na) | over-broad regex | — | negative lookahead `na\\b(?!\\s*\\()` | regression pair kept | true `bool x = na` still caught; v2.0 L55 passes |
| ERR-006 | G09 + card L6 over-strict (banned legal `[1]+lookahead_on`) | rule written from one source; full read found 3-source conflict C2 | — | LAW: lookahead_on legal ONLY with [1]-offset; G09 v1.2 | conflict register entry C2; both-direction regression | la_bad fails / la_good passes |
| ERR-007 | sim v1.2 crash invisible: blind str-patch no-opped + stderr→/dev/null → stale report read | patching own code from memory; suppressing the oracle | — | read-then-str_replace with verification; never swallow stderr on verification runs | FE-03 in sim header; rule applies to TOOLING too | exit-code + fresh-field check (median_escapes present) |
| ERR-009 | observation theater: OBS table reverse-narrated from existing code; zero numerals despite on-screen OHLC | extraction generated to justify output, not from pixels | shipping anyway | numeral rule: [READ] rows require literal image numbers; void otherwise | THE_CARD v2.1 numeral + gate-finality rules | his table fails numeral rule on all 9 rows |
| ERR-011 | external instance emitted //@version=5 with no canon scaffolding | PERSONA.md not loaded → no gate ran (SG silent-governance) | — | G01 pins version==6; PERSONA must be loaded as operating instruction; output contract mandates header+lineage+receipt | G01:VERSION_NOT_6 + PERSONA §0/§3 | new G01 fails the v5 code; all v6 artifacts still pass |
| ERR-010 | fabricated preflight report (unknown gate IDs, fake PASS) | verification narrated, not executed (ERR-004 externalized) | — | preflight-authenticity rule: verbatim paste, registry-valid gate IDs, exit line required | real run attached; registry G01–G15 canonical | real run: FAIL 4 vs claimed PASS |
| ERR-008 | shell brace-expansion silently failed (sh≠bash) | environment assumption | — | explicit paths; check returncode before proceeding | set -e habit + returncode check | rebuild succeeded with explicit mkdir |

## §4 CONFLICT REGISTER (canon contradictions, resolved · from full read)
C1 multiline: indented continuation is legal Pine [LAW]; single-line is the
   HOUSE emission standard; never start a line with an operator.
C2 lookahead_on: legal only with [1]-offset source → G09 v1.2, card A-add.
C3 typed na: required at declarations; nz/guards at use-sites. Both stand.
C4 strategy.*: Ω-ONE's ban is the indicator-product law; strategies are a
   separate legal file envelope (Holy Grail separation table).
C6 governance topology: GENIE/PineClarity treat rules as a flat active
   set; canon [GT] proves governance is an ORDERED sequence P0->P7.
   RESOLUTION: rules fire only at their precondition phase; reordering
   is a MAJOR-version change. (REWIRE_MAP.md.)
C5 persona output policy: PineClarity "output only ready-to-deploy code"
   vs canon's mandatory image gate + preflight receipt + no-claim-without-
   artifact. RESOLUTION: canon wins; code-only yields. Silent emission is
   the ERR-004/009/010 failure mode. (PERSONA §0.)

## §5 RECEIPTS & PROOFS INDEX (v1.1.0 layout · supersedes prior §5 per U-010)
§5a Files: THE_CARD.txt (law) · pine_preflight.py (14 gates; headers map
gate→taxonomy rule-ID) · MONOLITH.md (library; SHA-256 =
8c4a281d64c0841fe7728306b398a8d58f6f5c559c91e02b232c29f4f6e3b5b2 ; its §0.5
embeds the 51-source 100% coverage + integrity ledger) · events.json
([GT] log, append-only) · walkforward_sim.py (deterministic, seed
20260612 — running it IS the receipt) · two .pine.txt artifacts ·
CHECKSUMS.sha256 (every file here incl. this ledger; the bundle zip's own
hash is stated externally in chat at ship time).
§5b Embedded walk-forward key numbers (regenerable, v1.2 sim):
[GT] PRE t1–14: 6 escapes/14 turns, var 585 → POST t15–24: 0/10, var 35,
slope +0.35. [SYN 150-turn]: ALL-5 ruin 0.0 / 7 escapes · minus-R2 ruin
0.998 · {R2,R3,R5} ruin 0.0 / 8 escapes (model-minimum; operational
minimum = ALL-5 per [GT]). Edge invalidation V1–V7 as logged in U-009.
## §6 OPEN ITEMS (truth about what is NOT done)
O1 P1 shell AND SEQ_1234_v1_0.pine.txt await human TradingView compile
   verdict (R4). P2–P8 + SEQ-1234 sign-off locked until paste-back.
O2 Full-read batches 4–9 pending (AIO_v2, Ui.txt, MASTERLOCK, PineAgent
   prompts ×2, ERROR_SOLUTIONS, cheatsheets, checklist, INSTITUTIONAL
   VISUALS, giants structural pass) → then sequence/build-needs manifest.
O3 Sentinel v2.0 is compiler-UNTESTED. O4 Doji-sequence FSM read awaits
   human OBS verification (ERR-003 gate applies).
