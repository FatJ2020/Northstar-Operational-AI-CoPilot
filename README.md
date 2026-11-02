# Northstar Operational AI Copilot

**Status: Demo-ready governance + routing prototype**

An evidence-grounded, confidence-scored **decision-support** assistant for cross-functional operations — built on a governance framework that keeps humans accountable for every decision that matters.

> Demo project using a fictional company ("Northstar Systems", a B2B industrial IoT vendor) and **synthetic data**.  
> All names, figures and records are fictional.  
> AI supports decisions. AI does not own decisions.

---

## Why this project exists

Teams in engineering and manufacturing organisations spend significant effort searching across customer feedback, supplier updates, engineering actions, product roadmaps and commercial records. Important decisions are delayed because information is fragmented.

This project demonstrates how Generative AI can support **evidence retrieval, operational review and decision preparation** while maintaining **human accountability** for the decision itself.

---

## Core design principle

| Rule | Meaning |
|------|---------|
| AI supports decisions | Retrieve, summarise, score confidence, prepare the file |
| AI does not own decisions | Commercial, contractual, high-risk and external actions stay with named humans |
| Confidence is a routing signal | High confidence + administrative + low risk → may go to digest; everything else → human review |

---

## What is actually runnable today

```bash
python src/copilot_pipeline_example.py
```

This dependency-free sketch:
- scores synthetic findings on confidence
- routes administrative vs commercial / high-risk items
- prints the owner and the reason for each route

No API key, no vector store, no live LLM required for the portfolio demo.

---

## Governance documents

| Document | What it defines |
|----------|-----------------|
| [docs/governance/confidence_policy.md](docs/governance/confidence_policy.md) | How confidence is scored and what each band allows |
| [docs/governance/decision_matrix.md](docs/governance/decision_matrix.md) | What AI may auto-flag vs what always needs a human |
| [docs/governance/human_vs_ai.md](docs/governance/human_vs_ai.md) | Explicit split of responsibilities |

**Principle:** Final accountability for financial risk, customer commitments, product strategy, supplier governance and operational performance remains with **named human owners**.

---

## Example use cases

- Weekly Operations Reviews  
- Supplier Escalation Reviews  
- Customer Risk Assessments  
- NPI Readiness Reviews  
- Sales Opportunity Risk Reviews  
- Executive Decision Preparation  

---

## Intended full stack (future)

Python · LangChain · ChromaDB · GPT/Claude · Streamlit  

This repository focuses on **data + governance design + decision logic**. The `src/copilot_pipeline_example.py` file is the transparent core of the routing policy.

---

## Portfolio workbook

See `Northstar_Portfolio_Workbook.xlsx` for:
- Overview & confidence bands  
- Decision matrix  
- Demo routing results  
- Interview Q&A  
- One-minute pitch  

---

## Related projects

- [Agent Development Lifecycle (ADL)](https://github.com/FatJ2020/agent-development-lifecycle) — risk-gated lifecycle + deterministic trace evaluation  
- [Industrial AI Evaluation Framework](https://github.com/FatJ2020/Industrial-AI-evaluation-framework) — rubric for evaluating industrial LLM answers  

Together: **evaluate → govern → lifecycle**.

---

## Limitations

- Synthetic data only  
- Pipeline example is a sketch of confidence + routing, not a production RAG system  
- Not a safety case or certification  
- Never put confidential employer data in this repository  

---

## License

MIT License — see [LICENSE](LICENSE).
