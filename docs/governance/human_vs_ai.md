# Human vs AI — Explicit Split of Responsibilities

## Core principle
**AI supports decisions. AI does not own decisions.**

Final accountability for financial risk, customer commitments, product strategy, supplier governance and operational performance remains with **named human owners**.

## Responsibility split

| Area | AI (Copilot) may | AI must not | Human owner must |
|------|------------------|-------------|------------------|
| Information retrieval | Search approved sources, return citations | Invent sources or hide uncertainty | Validate critical evidence when stakes are high |
| Summarisation | Draft concise findings linked to evidence IDs | Present drafts as final decisions | Edit, accept or reject the draft |
| Risk flagging | Highlight anomalies and missing approvals | Close a risk without human sign-off | Accept, escalate or dismiss the risk |
| Routing | Recommend digest vs human review based on policy | Override the governance policy | Set and change the policy |
| External action | — | Issue PO, release payment, send customer commitment, change production plan | Authorise every external action |
| Audit trail | Log evidence IDs, confidence, route and owner | Operate without an auditable trail | Ensure the trail is retained and reviewable |

## Why this matters for industrial settings
In manufacturing and supply-chain environments, an incorrect autonomous action can create quality escapes, commercial disputes or safety issues.  
Keeping a named human in the loop for consequential decisions is therefore a design requirement, not an optional extra.

## Portfolio demonstration
The Python sketch `src/copilot_pipeline_example.py` implements a minimal version of this split: it can route low-risk administrative findings to a digest, and it forces human review for commercial and high-risk items.
