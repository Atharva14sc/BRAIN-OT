import joblib
import pandas as pd

class MLDetector:

    def __init__(self):

        self.model = joblib.load(
            r"C:\Atharva\BRAIN-OT\models\modbus_model.pkl"
        )

    def predict(self, packet_info):

        try:

            features = pd.DataFrame([{
    "packet_length": packet_info["packet_length"],
    "destination_port": packet_info["destination_port"] or 0,
    "source_port": packet_info["source_port"] or 0,
    "is_tcp": 1 if packet_info["protocol"] == "TCP" else 0
}])

            prediction = self.model.predict(features)[0]

            return prediction

        except Exception as e:

            print("ML Error:", e)
            return 0