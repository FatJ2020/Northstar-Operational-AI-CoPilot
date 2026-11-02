# Decision Matrix — What AI May Flag vs. What Always Needs a Human

## Purpose
Make the boundary between “AI can prepare” and “human must decide” explicit and auditable.

## Matrix

| Decision type | Examples | AI role | Human role | Default route |
|---------------|----------|---------|------------|---------------|
| Administrative / operational status | OTIF trend, open action count, meeting notes summary | Retrieve, summarise, flag anomalies | Review digest, correct if needed | Auto-digest if high confidence + low risk |
| Cross-functional visibility | Overdue actions across teams, unowned items | Aggregate and highlight | Confirm ownership and dates | Human review |
| Supplier risk signal | Capacity alert, quality escape trend | Surface evidence and draft risk note | Decide escalation and commercial action | Human review |
| Customer / commercial risk | Renewal risk, pricing exception, commitment change | Prepare evidence pack | Own the customer decision | **Always human** |
| NPI / launch readiness | Open PPAP items, missing approvals | List gaps against checklist | Gate the launch decision | **Always human** |
| Financial / contractual | Payment release, PO issue, contract deviation | **No autonomous action** | Sole decision owner | **Always human** |
| Policy / safety / compliance | Anything touching regulated or safety-critical process | Flag only | Formal approval required | **Always human** |

## Summary rule
> If the consequence of being wrong is commercial, contractual, safety-related or reputational, the Copilot prepares the file and a **named human** decides.
