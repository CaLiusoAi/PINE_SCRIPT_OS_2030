# SPEC — SEQ-1234 EQUAL-HIGH REJECTION (active build target)
GATE STATUS: RULED 2026-06-12 — (a)="A", (b)=image-9 render contract.
Phases 2-4 COMPLETE → SEQ_1234_v1_0.pine.txt (real preflight PASS 15/0
--irts). Awaits human TradingView compile verdict (R4) before sign-off.

## GROUND TRUTH — 9 spec images (NQ1! 15m, 10:15–11:00 AM) + target render
OBS-01 [READ] Badges 1→4 placed one per screenshot on four consecutive candles.
OBS-02 [EST]  C1: green impulse, body ≈30,545→30,600, lower wick ≈30,538.
OBS-03 [EST]  C2: green continuation, body ≈30,598→30,658, upper wick 30,692.25, deep lower wick ≈30,565.
OBS-04 [READ] C3 hover OHLC: O 30,651.50 · H 30,692.25 · L 30,651.25 · C 30,670.00 → C2.high == C3.high EXACTLY (equal highs).
OBS-05 [READ] Magenta horizontal line at the equal-high level (30,692.25; later nudged 30,693.00) spanning the sequence.
OBS-06 [EST]  C4: red rejection — open ≈30,668, close ≈30,635, upper wick ≈30,673; approaches level zone, closes hard away.
OBS-07 [READ] Blue up-arrow annotation: C1 low through C2 = impulse leg (stages 1–2).
OBS-08 [READ] Crimson down-arrow through C4 to its low = rejection/markdown at stage 4; small dark-red arrow above C4.
OBS-09 [READ] Orange solid ≈30,668–670 (C3 body top / C4 open shelf); orange dotted ≈30,634 (C4 close zone).
OBS-10 [READ] TARGET RENDER (image 9, NQ1! 1m): teal pins "1","2" BELOW their green bars · cyan pin "3" ABOVE the level-tag bar · red pin "4" ABOVE the red rejection bar with red down-arrow · magenta line at 29,760 across the 3–4 zone · orange dashed ≈29,744 · price then drops ≈29,755→29,690. Indicator output must reproduce this construction.
OBS-11 [READ] Failure evidence (IMG_9589/9590): old waterfall code printed scattered arrows/X in an uptrend — zero geometric overlap with OBS-10.

## PENDING RULINGS (human-only)
(a) Sequence = 1 impulse green · 2 continuation green whose wick sets level ·
    3 bar printing EQUAL HIGH at that level · 4 red bar REJECTING it → short.
(b) Deliverable = detector + image-9 rendering: numbered pins 1–4, magenta
    sweep line at the equal-high level, red down-arrow on bar 4.
