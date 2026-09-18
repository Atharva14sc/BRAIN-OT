from process_anomaly_detector import ProcessAnomalyDetector

detector = ProcessAnomalyDetector()

result = detector.detect(
    temperature=95,
    pressure=130,
    vibration=20
)

print(result)