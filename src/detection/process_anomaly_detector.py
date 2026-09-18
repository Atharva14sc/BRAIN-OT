class ProcessAnomalyDetector:

    def detect(
        self,
        temperature,
        pressure,
        vibration
    ):

        anomalies = []

        if temperature > 80:
            anomalies.append("High Temperature")

        if pressure > 120:
            anomalies.append("High Pressure")

        if vibration > 15:
            anomalies.append("Abnormal Vibration")

        return {
            "anomaly_detected": len(anomalies) > 0,
            "reasons": anomalies
        }