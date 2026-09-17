from threat_decision_engine import ThreatDecisionEngine

engine = ThreatDecisionEngine()

result = engine.evaluate(
    bati_score=45,
    bati_status="SUSPICIOUS",
    threat_type="injection",
    anomaly_detected=True
)

print(result)