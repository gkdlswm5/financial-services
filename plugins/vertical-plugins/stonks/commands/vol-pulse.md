---
description: Run the options/volatility pulse on the major indexes and top movers
argument-hint: "[indexes or tickers, e.g. 'SPX NDX RUT']"
---

Load the `vol-pulse` skill and produce a point-in-time options/volatility dashboard:
IV rank & percentile, term-structure slope, 25-delta skew, vol risk premium (IV vs realized),
the VIX complex, and put/call ratios — then tie the vol regime back to the crowd-positioning
2×2 from `event-deep-dive`.

Use the LSEG `option-vol-analysis` engine for the vol surface and Greeks. Mark any
options-volume/flow cell `[needs feed]` if no OPRA-class feed is connected. Timestamp every
figure. Pair GLD with gold and SLV with silver.

If indexes/tickers are provided, use them; otherwise default to SPX, NDX, RUT.

Tip: schedule it with `/loop 30m /stonks:vol-pulse` for a recurring read.
