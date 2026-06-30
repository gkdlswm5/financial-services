---
description: Combined micro/macro event deep dive + options/volatility pulse
argument-hint: "[scope, e.g. 'US large-cap' or a watchlist]"
---

Run the full market read in two passes and stitch them together:

1. Load `event-deep-dive` — the micro/macro event scan with the Buffett signal-vs-noise sort,
   the sentiment-vs-fundamentals 2×2, and the macro consensus heat strip.
2. Load `vol-pulse` — IV rank/percentile, term structure, skew, vol risk premium, the VIX
   complex, and put/call ratios.
3. **Stitch:** overlay the vol regime onto the event 2×2 — cheap/calm vol makes the
   MOMENTUM-CROWDED corner more dangerous (and protection cheap); rich/fearful vol pays you
   in the OWN IT corner. Lead with the gap between crowd positioning and durable value.

Cite/timestamp every figure; mark `[UNSOURCED]` / `[needs feed]` honestly. Pair GLD with
gold and SLV with silver.

If a scope is provided, use it; otherwise default to broad US equities + the macro spine.

Tip: schedule with `/loop 1h /stonks:market-pulse`.
