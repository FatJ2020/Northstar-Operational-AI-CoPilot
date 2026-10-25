# Northstar Operational AI Copilot

**An evidence-grounded, confidence-scored decision-support assistant for cross-functional
operations — built on a governance framework that keeps humans accountable for every decision
that matters. Status: Demo-ready governance + RAG prototype**

> Demo project using a fictional company ("Northstar Systems", a B2B industrial IoT vendor) and
> synthetic data, built to demonstrate how Generative AI can support operational and commercial
> decision-making in an engineering/manufacturing business. All names, figures and records are
> fictional — see [`docs/source_data/`](docs/source_data/).

---

## Project Background

This project was inspired by real operational challenges commonly found in engineering and
manufacturing organisations.

Teams often spend significant effort searching across:

- Customer feedback
- Supplier updates
- Engineering actions
- Product roadmaps
- Commercial records

Important decisions are frequently delayed because information is fragmented across multiple
systems. This project demonstrates how Generative AI can support evidence retrieval, operational
review and decision preparation — **while maintaining human accountability** for the decision
itself.

---

## Example Copilot Output

![Northstar Copilot sample output](images/dashboard-overview.png)

See [`CASE_STUDY.md`](CASE_STUDY.md) for the full worked example behind this output, and
[`docs/governance/sample_decision_review.md`](docs/governance/sample_decision_review.md) for the
complete five-finding version.

---

## System Architecture

![System architecture](images/architecture.png)

Data from five operational domains is retrieved, analysed and turned into a confidence-scored,
evidence-linked recommendation — which is then routed either straight to the operational digest
(high confidence, administrative) or to a named human owner for review (everything commercial,
contractual or strategic). See [`docs/governance/workflow.md`](docs/governance/workflow.md) for
the full stage-by-stage breakdown, and
[`src/copilot_pipeline_example.py`](src/copilot_pipeline_example.py) for a short, runnable sketch
of the confidence-and-routing logic in Python.

---

## Decision Support & Governance Layer

The Copilot is designed as a **decision-support system**, not an automated decision-maker. This
is not an afterthought — it is the core design constraint behind the whole project:

| Document | What it defines |
|---|---|
| [`docs/governance/workflow.md`](docs/governance/workflow.md) | End-to-end flow from question to audited decision |
| [`docs/governance/decision_matrix.md`](docs/governance/decision_matrix.md) | What the AI may auto-flag vs. what always needs a human |
| [`docs/governance/human_vs_ai.md`](docs/governance/human_vs_ai.md) | Explicit split of responsibilities |
| [`docs/governance/confidence_policy.md`](docs/governance/confidence_policy.md) | How confidence is scored and what happens at each band |
| [`docs/governance/escalation_framework.md`](docs/governance/escalation_framework.md) | What triggers escalation, and to whom |
| [`docs/governance/sample_decision_review.md`](docs/governance/sample_decision_review.md) | A full worked example of Copilot output |

**Principle:** AI supports decisions. AI does not own decisions. Final accountability for
financial risk, customer commitments, product strategy, supplier governance and operational
performance remains with named human owners throughout.

---

## Business Value

The Copilot reduces time spent searching across disconnected operational records.

**Example use cases:**

- Weekly Operations Reviews
- Supplier Escalation Reviews
- Customer Risk Assessments
- NPI Readiness Reviews
- Sales Opportunity Risk Reviews
- Executive Decision Preparation

**Expected Benefits:**

- Faster root-cause analysis
- Reduced information-retrieval time
- Improved traceability
- Consistent decision preparation
- Improved cross-functional visibility

---

## Example Questions

**Customer**
- Which customer issues recur most frequently?
- Which accounts are at renewal risk?

**Operations**
- What operational risks need escalation?
- Which actions are overdue or unowned?

**Supply Chain**
- Which supplier issues threaten customer commitments?

**Commercial**
- Which opportunities are blocked by product gaps?

**NPI**
- What readiness items remain open before launch?

**Executive**
- What decisions require leadership attention this week?

---

## Data & Documents

12 synthetic source documents (the Copilot's knowledge base) plus the governance layer above, all
compiled into one workbook for easy review:

- [`Northstar_Systems_Demo_Data_v2_Governance.xlsx`](Northstar_Systems_Demo_Data_v2_Governance.xlsx) — everything in one file, tab per document
- [`docs/source_data/`](docs/source_data/) — the same 12 documents as standalone `.md` / `.csv` files, ready for a retrieval pipeline

| # | Domain | File | Example question |
|---|---|---|---|
| 1 | Product | `product_roadmap_q3.md` | What are the roadmap's main Q3 goals and open items? |
| 2 | Customer Experience | `customer_feedback_q3.csv` | Which customer pain points recur most frequently? |
| 3 | Customer Support | `support_incidents.md` | Which incidents need priority escalation? |
| 4 | Market | `market_research_europe.md` | Which market needs are backed by evidence? |
| 5 | Commercial / Sales | `sales_pipeline.csv` | Which opportunities need follow-up or are at risk? |
| 6 | Quotation | `commercial_quote_001.md` | What cost assumptions and risks sit behind this quote? |
| 7 | Customer Requirements | `customer_requirements_001.md` | What gaps exist between customer requirements and current capability? |
| 8 | Supply Chain | `supplier_status.csv` | Which supplier issues could affect customer commitments? |
| 9 | NPI | `npi_readiness.md` | What NPI items are still open? |
| 10 | Operations | `weekly_operations_review.md` | What's affecting cost, quality or delivery this week? |
| 11 | Program / Project | `project_action_log.csv` | Which actions are overdue, blocked, or unowned? |
| 12 | Decisions | `decision_log.md` | Which decisions are approved vs. pending? |

---

## Repository Structure

```
README.md
CASE_STUDY.md
Northstar_Systems_Demo_Data_v2_Governance.xlsx
images/
  architecture.png
  dashboard-overview.png
docs/
  source_data/            12 source documents (the Copilot's knowledge base)
  governance/              Decision support & governance framework (6 documents)
src/
  copilot_pipeline_example.py   Runnable sketch of the confidence/routing logic
```

---

## Intended Tech Stack

A first version would use: **Python** for core logic, **LangChain** for document loading and
orchestration, **ChromaDB** as the vector store, and **GPT / Claude** for evidence-grounded
reasoning, with a **Streamlit** front end for question input, source citations and an action
list. This repository documents the data, the governance design and the decision logic
([`src/copilot_pipeline_example.py`](src/copilot_pipeline_example.py)) that the pipeline is built
around.

---

## Related Project

This project pairs with
[**industrial-ai-evaluation-framework**](https://github.com/FatJ2020/industrial-ai-evaluation-framework) —
a structured methodology for evaluating enterprise LLM responses (accuracy, evidence-based
reasoning, process compliance, risk awareness, traceability) across manufacturing, quality and
supply-chain domains. Together they cover both sides of enterprise AI adoption: **evaluating**
whether an AI response can be trusted, and **governing** how an AI system is allowed to act on
it.
