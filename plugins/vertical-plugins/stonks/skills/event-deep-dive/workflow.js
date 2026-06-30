export const meta = {
  name: 'event-deep-dive',
  description: 'Dynamic micro/macro event deep dive: fan-out web search, adversarial verify, Buffett signal-vs-noise + crowd-sentiment analysis, with a parameterized & regime-aware horizon',
  phases: [
    { title: 'Search', detail: 'parallel angle searches across macro spine + hot sectors + forward catalysts (+ regime analogs)' },
    { title: 'Verify', detail: 'adversarial fact-check of each angle’s events (3-vote, needs 2/3 to refute)' },
    { title: 'Analyze', detail: 'Buffett signal/noise + sentiment 2x2 + macro heat strip over the verified set' },
  ],
}

// ---------------------------------------------------------------------------
// Dynamic horizon — driven by args (all optional):
//   { lookbackDays, forwardDays, mode, universe, sectors, analogs }
//   mode: "fixed" | "auto" (auto = let the search agents reach back to the last
//          comparable analog when a regime break is in-window)
//   universe: "whole-market" (default) | "sector" | "watchlist"
//   sectors:  array of sector labels to deep-dive (defaults to the hottest few)
//   analogs:  array of past episodes to pull in for context (e.g. ["2022 oil shock"])
// ---------------------------------------------------------------------------
const A = (typeof args === 'object' && args) ? args : {}
const lookbackDays = A.lookbackDays || 90
const forwardDays = A.forwardDays || 90
const mode = A.mode || 'auto'
const universe = A.universe || 'whole-market'
const sectors = A.sectors || ['AI / semiconductors', 'energy', 'financials']
const analogs = A.analogs || []

// Schemas are deliberately permissive (plain strings, few required fields) to avoid
// StructuredOutput retry-cap failures.
const EVENTS_SCHEMA = {
  type: 'object',
  properties: {
    events: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          headline: { type: 'string' },
          layer: { type: 'string', description: 'macro or micro' },
          category: { type: 'string' },
          date: { type: 'string' },
          summary: { type: 'string' },
          keyFigures: { type: 'string', description: 'concrete numbers, or [UNSOURCED]' },
          source: { type: 'string', description: 'publication and/or URL, or [UNSOURCED]' },
        },
        required: ['headline', 'summary'],
      },
    },
  },
  required: ['events'],
}
const VERIFIED_SCHEMA = {
  type: 'object',
  properties: {
    events: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          headline: { type: 'string' }, layer: { type: 'string' }, category: { type: 'string' },
          date: { type: 'string' }, summary: { type: 'string' }, keyFigures: { type: 'string' },
          source: { type: 'string' },
          confidence: { type: 'string', description: 'supported, uncertain, or refuted' },
          verifyNote: { type: 'string' },
        },
        required: ['headline', 'confidence'],
      },
    },
  },
  required: ['events'],
}
const ANALYSIS_SCHEMA = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          headline: { type: 'string' }, layer: { type: 'string' }, category: { type: 'string' },
          crowdReaction: { type: 'string' },
          changesIntrinsicValue: { type: 'string', description: 'yes / no / partial' },
          classification: { type: 'string', description: 'SIGNAL / NOISE / NOISE->BUY / SIGNAL->AVOID' },
          priceVsValue: { type: 'string', description: 'cheaper / dearer / unchanged' },
          circleOfCompetence: { type: 'string', description: 'in / out / edge' },
          marginOfSafety: { type: 'string' },
          crowdAxis: { type: 'string', description: 'bullish / bearish / neutral' },
          fundamentalsAxis: { type: 'string', description: 'improving / deteriorating / stable' },
          quadrant: { type: 'string', description: 'OWN IT / AVOID-FADE / FALLING KNIFE / MOMENTUM-CROWDED' },
          horizonDayTrader: { type: 'string' }, horizonHedgeFund: { type: 'string' },
          horizonLongOnly: { type: 'string' }, horizonOwner: { type: 'string' },
        },
        required: ['headline', 'classification', 'quadrant'],
      },
    },
  },
  required: ['items'],
}
const HEAT_SCHEMA = {
  type: 'object',
  properties: {
    dimensions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' }, tilt: { type: 'string' }, direction: { type: 'string' },
          intensity: { type: 'string', description: '1-5' }, note: { type: 'string' },
        },
        required: ['name', 'tilt'],
      },
    },
  },
  required: ['dimensions'],
}

// Build the search angles from the dynamic config.
const MACRO_ANGLES = [
  { key: 'rates', label: 'Fed & rates', q: 'Federal Reserve FOMC interest rate decision dot plot monetary policy outlook' },
  { key: 'inflation', label: 'Inflation & jobs', q: 'US CPI PCE inflation and nonfarm payrolls jobs report latest' },
  { key: 'geo-oil-usd', label: 'Geopolitics / oil / USD', q: 'geopolitics oil price crude WTI Brent US dollar index DXY markets latest' },
  { key: 'metals', label: 'Gold & silver (GLD/SLV)', q: 'gold price silver price GLD SLV ETF latest precious metals move' },
]
const SECTOR_ANGLES = sectors.map((s, i) => ({
  key: `sector-${i}`, label: s, layerHint: 'micro',
  q: `${s} sector bellwether companies earnings guidance M&A regulatory news latest`,
}))
const FORWARD_ANGLE = {
  key: 'forward', label: `Forward catalysts (next ~${forwardDays}d)`,
  q: 'upcoming market catalysts earnings calendar FOMC meeting dates economic data next quarter',
}
const ANALOG_ANGLES = (mode === 'auto' ? analogs : []).map((ep, i) => ({
  key: `analog-${i}`, label: `Regime analog: ${ep}`,
  q: `${ep} market impact what happened how it resolved historical comparison`,
}))

const ANGLES = universe === 'watchlist'
  ? [...MACRO_ANGLES, ...SECTOR_ANGLES, FORWARD_ANGLE, ...ANALOG_ANGLES]
  : [...MACRO_ANGLES, ...SECTOR_ANGLES, FORWARD_ANGLE, ...ANALOG_ANGLES]

log(`Horizon: -${lookbackDays}d / +${forwardDays}d · mode=${mode} · universe=${universe} · ${ANGLES.length} angles`)

const searchFn = (angle) => agent(
  `You are a markets research analyst. Use WebSearch (and WebFetch on the best results) to gather REAL, CURRENT events for this angle.

ANGLE: ${angle.label}
SEED QUERY: "${angle.q}"
HORIZON: look back ~${lookbackDays} days and forward ~${forwardDays} days from today.${angle.key.startsWith('analog') ? ' This is a HISTORICAL analog — summarize what happened and how it resolved, for context.' : ''}
Run 2-4 searches with varied phrasing. Pull concrete events: what happened, the date, the hard numbers (levels, % moves, bps, EPS, prices), and the source.

Rules:
- Real, sourced facts only. If you cannot source a figure, write [UNSOURCED] rather than inventing it.
- layer = "${angle.layerHint || 'macro'}" unless an item is clearly the other.
- For the gold/silver angle, ALWAYS report the GLD ETF level with gold spot and the SLV ETF level with silver spot.
- For the forward angle, items are UPCOMING (future-dated) catalysts.
- Aim for the 4-8 most market-moving events. Quality over quantity.

Return JSON via the structured output tool.`,
  { label: `search:${angle.key}`, phase: 'Search', schema: EVENTS_SCHEMA }
)

const verifyFn = (prev, angle) => {
  const events = (prev && Array.isArray(prev.events)) ? prev.events : []
  if (!events.length) return { events: [] }
  return agent(
    `You are an adversarial fact-checker. For EACH candidate event for angle "${angle.label}", try to REFUTE it: is the claim real, the figure plausible and correctly attributed, the date right? Use WebSearch to spot-check doubtful ones.

confidence: "supported" (corroborated), "uncertain" (can't corroborate / weak / [UNSOURCED]), "refuted" (contradicted — keep but flag). Default to "uncertain" when unsure rather than dropping. Add a one-line verifyNote and preserve all original fields.

EVENTS JSON:
${JSON.stringify(events)}

Return the same events annotated, via the structured output tool.`,
    { label: `verify:${angle.key}`, phase: 'Verify', schema: VERIFIED_SCHEMA }
  )
}

phase('Search')
const verified = await pipeline(ANGLES, searchFn, verifyFn)

const allEvents = verified.filter(Boolean).flatMap(v => (v && Array.isArray(v.events)) ? v.events : [])
log(`Collected ${allEvents.length} verified events across ${ANGLES.length} angles`)

const forAnalysis = allEvents
  .filter(e => (e.confidence || '').toLowerCase() !== 'refuted')
  .map(e => ({ headline: e.headline, layer: e.layer, category: e.category, date: e.date, summary: e.summary, keyFigures: e.keyFigures, confidence: e.confidence }))

phase('Analyze')
const [analysis, heat] = await parallel([
  () => agent(
    `You are Warren Buffett's research associate. For EACH verified event below, fill the analysis fields.

Buffett discipline:
- classification: SIGNAL (changes durable intrinsic value / owner-earnings) vs NOISE (just the quote/mood). Use "NOISE->BUY" when the crowd overreacted on something that doesn't impair value, "SIGNAL->AVOID" when fundamentals genuinely deteriorated.
- changesIntrinsicValue: yes / no / partial.
- crowdReaction: how price/consensus reacted and the prevailing narrative.
- priceVsValue: cheaper / dearer / unchanged.
- circleOfCompetence: in / out / edge — say plainly when a macro event is un-forecastable.
- marginOfSafety: one line.
- 2x2: crowdAxis (bullish/bearish/neutral), fundamentalsAxis (improving/deteriorating/stable), quadrant in {OWN IT, AVOID-FADE, FALLING KNIFE, MOMENTUM-CROWDED}. OWN IT = crowd bearish but fundamentals fine; MOMENTUM-CROWDED = crowd bullish but fundamentals cracking; AVOID-FADE = crowd bullish, fundamentals only ok; FALLING KNIFE = crowd bearish, fundamentals bad.
- horizon readings: one short phrase each for how a dayTrader, hedgeFund, longOnly analyst, and longTermOwner reads THIS event.

EVENTS JSON:
${JSON.stringify(forAnalysis)}

Return via the structured output tool.`,
    { label: 'buffett+sentiment', phase: 'Analyze', schema: ANALYSIS_SCHEMA, effort: 'high' }
  ),
  () => agent(
    `From the verified MACRO events below, produce a MACRO CONSENSUS HEAT STRIP. Include EXACTLY these dimensions in order: RATES, INFLATION, GROWTH, POLICY, USD, OIL, "GOLD (GLD)", "SILVER (SLV)". For each: tilt, direction (up/down/flat), intensity (1-5 = how crowded the consensus is), terse note. Ground it in the events; if a dimension is thin, say so.

EVENTS JSON:
${JSON.stringify(forAnalysis.filter(e => (e.layer || '').toLowerCase() === 'macro'))}

Return via the structured output tool.`,
    { label: 'macro-heat-strip', phase: 'Analyze', schema: HEAT_SCHEMA, effort: 'high' }
  ),
])

return {
  config: { lookbackDays, forwardDays, mode, universe, sectors, analogs },
  counts: {
    total: allEvents.length,
    supported: allEvents.filter(e => (e.confidence || '').toLowerCase() === 'supported').length,
    uncertain: allEvents.filter(e => (e.confidence || '').toLowerCase() === 'uncertain').length,
    refuted: allEvents.filter(e => (e.confidence || '').toLowerCase() === 'refuted').length,
  },
  events: allEvents,
  analysis: (analysis && analysis.items) ? analysis.items : [],
  heat: (heat && heat.dimensions) ? heat.dimensions : [],
}
