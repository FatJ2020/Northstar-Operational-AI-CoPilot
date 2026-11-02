# Confidence Policy

## Purpose
Define how the Copilot assigns a confidence score to each finding and what the system is allowed to do at each confidence band.

## Design principle
Confidence is a **routing signal**, not a licence to act.  
Even a high-confidence finding that touches commercial, contractual or strategic risk is routed to a named human owner.

## Simplified scoring factors (portfolio version)

| Factor | Effect on score |
|--------|------------------|
| Number of supporting evidence IDs | Increases confidence |
| Agreement across sources | Increases confidence |
| Risk level = high | Decreases confidence / raises human threshold |
| Explicit `requires_human` flag | Caps confidence and forces human route |
| Missing or conflicting evidence | Decreases confidence |

## Confidence bands and actions

| Band | Score range | Allowed system action |
|------|-------------|------------------------|
| High | ≥ 0.75 | May auto-route to operational digest **only if** domain is administrative and risk is low |
| Medium | 0.50 – 0.74 | Always human review |
| Low | < 0.50 | Human review + explicit evidence gap note |

## Hard rules (non-negotiable)
1. Commercial, contractual, pricing, customer-commitment and NPI-launch decisions → **always human**.
2. Any finding with `risk_level = high` → **always human**.
3. Any finding that would trigger an external action (PO, payment, customer communication) → **always human**.
4. Confidence never replaces named-human accountability.

## Portfolio note
The numeric thresholds and weights in `src/copilot_pipeline_example.py` are illustrative.  
A production system would calibrate thresholds with historical decisions and human adjudication.
