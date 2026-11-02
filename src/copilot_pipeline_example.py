"""
Northstar Operational AI Copilot — Confidence & Routing sketch
--------------------------------------------------------------
Demonstrates the core design rule:
  AI supports decisions. AI does not own decisions.

- Scores a synthetic finding on confidence.
- Routes high-confidence administrative items to an operational digest.
- Routes everything commercial / contractual / strategic to a named human owner.

This is a transparent, dependency-free example for portfolio demonstration.
No live LLM or vector store is called.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Finding:
    finding_id: str
    domain: str          # e.g. "operations", "commercial", "supply_chain", "npi"
    summary: str
    evidence_ids: List[str]
    risk_level: str      # "low" | "medium" | "high"
    requires_human: bool


@dataclass
class RoutedDecision:
    finding_id: str
    confidence: float
    route: str           # "auto_digest" | "human_review"
    owner: Optional[str]
    reason: str


# ---- Confidence policy (simplified) -----------------------------------------
def score_confidence(finding: Finding) -> float:
    """
    Very small, explainable heuristic for the portfolio demo.
    Real systems would combine retrieval scores, source agreement, etc.
    """
    score = 0.40
    # More evidence → higher confidence
    score += min(len(finding.evidence_ids) * 0.12, 0.36)
    # Risk adjusts confidence requirement (high risk is harder to auto-route)
    if finding.risk_level == "low":
        score += 0.10
    elif finding.risk_level == "high":
        score -= 0.15
    # Explicit human flag
    if finding.requires_human:
        score = min(score, 0.55)
    return round(max(0.0, min(1.0, score)), 2)


# ---- Routing policy ---------------------------------------------------------
ADMIN_DOMAINS = {"operations", "support"}
HUMAN_DOMAINS = {"commercial", "supply_chain", "npi", "executive", "customer"}

OWNER_MAP = {
    "commercial": "Sales Ops Lead",
    "supply_chain": "Supply Chain Manager",
    "npi": "NPI Program Manager",
    "executive": "Operations Director",
    "customer": "Customer Success Lead",
    "operations": "Ops Controller",
    "support": "Support Manager",
}


def route_finding(finding: Finding, confidence: float) -> RoutedDecision:
    """
    Core governance rule:
    - High confidence + administrative domain → may go to operational digest
    - Anything commercial / contractual / strategic / high-risk → human review
    """
    if finding.requires_human or finding.risk_level == "high":
        return RoutedDecision(
            finding_id=finding.finding_id,
            confidence=confidence,
            route="human_review",
            owner=OWNER_MAP.get(finding.domain, "Named Human Owner"),
            reason="High risk or explicit human-required flag",
        )

    if finding.domain in ADMIN_DOMAINS and confidence >= 0.75:
        return RoutedDecision(
            finding_id=finding.finding_id,
            confidence=confidence,
            route="auto_digest",
            owner=None,
            reason="High confidence administrative finding",
        )

    return RoutedDecision(
        finding_id=finding.finding_id,
        confidence=confidence,
        route="human_review",
        owner=OWNER_MAP.get(finding.domain, "Named Human Owner"),
        reason="Domain requires human accountability or confidence below threshold",
    )


# ---- Demo -------------------------------------------------------------------
def main() -> None:
    demo_findings = [
        Finding(
            finding_id="F-001",
            domain="operations",
            summary="Weekly OTIF dropped 4 points; root cause linked to line 3 changeover.",
            evidence_ids=["OPS-WEEKLY-42", "LINE3-LOG"],
            risk_level="low",
            requires_human=False,
        ),
        Finding(
            finding_id="F-002",
            domain="commercial",
            summary="Key account renewal at risk due to unresolved quality escapes.",
            evidence_ids=["CSAT-881", "ESCAPE-12"],
            risk_level="high",
            requires_human=True,
        ),
        Finding(
            finding_id="F-003",
            domain="supply_chain",
            summary="Single-source supplier capacity alert for Q4 critical component.",
            evidence_ids=["SUP-CAP-09"],
            risk_level="medium",
            requires_human=False,
        ),
    ]

    print("Northstar Copilot — Confidence & Routing Demo\n" + "=" * 50)
    for finding in demo_findings:
        conf = score_confidence(finding)
        decision = route_finding(finding, conf)
        print(f"\n[{finding.finding_id}] {finding.summary[:70]}...")
        print(f"  Domain     : {finding.domain} | Risk: {finding.risk_level}")
        print(f"  Confidence : {decision.confidence:.2f}")
        print(f"  Route      : {decision.route.upper()}")
        print(f"  Owner      : {decision.owner or '—'}")
        print(f"  Reason     : {decision.reason}")

    print("\n" + "=" * 50)
    print("Principle: AI supports decisions. AI does not own decisions.")


if __name__ == "__main__":
    main()
