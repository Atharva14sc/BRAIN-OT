class ThreatDecisionEngine:

    def __init__(self):

        self.modbus_ports = {
            502,
            102,
            44818,
            20000
        }

    def evaluate(
        self,
        bati_score,
        bati_status,
        threat_type,
        anomaly_detected
    ):

        confidence = 0
        reasons = []

        # ==================================
        # BATI Evaluation
        # ==================================

        if bati_status == "CRITICAL":

            confidence += 70

            reasons.append(
                "Critical BATI Score"
            )

        elif bati_status == "SUSPICIOUS":

            confidence += 40

            reasons.append(
                "Suspicious BATI Activity"
            )

        elif bati_status == "MONITOR":

            confidence += 15

            reasons.append(
                "Monitoring Recommended"
            )

        # ==================================
        # ML Threat Detection
        # ==================================

        if threat_type not in [
            "normal",
            "N/A",
            None
        ]:

            confidence += 30

            reasons.append(
                f"ML Threat Detected ({threat_type})"
            )

        # ==================================
        # PLC Anomaly Detection
        # ==================================

        if anomaly_detected:

            confidence += 40

            reasons.append(
                "PLC Anomaly Detected"
            )

        # ==================================
        # Verdict Generation
        # ==================================

        if confidence >= 80:

            status = "CRITICAL"

        elif confidence >= 50:

            status = "HIGH RISK"

        elif confidence >= 20:

            status = "MONITOR"

        else:

            status = "TRUSTED"

        return {
            "status": status,
            "confidence": min(confidence, 100), 
            "reasons": reasons
        }