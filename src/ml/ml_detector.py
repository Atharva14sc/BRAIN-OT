import joblib


class MLDetector:

    def __init__(self):

        self.model = joblib.load(
            r"C:\Atharva\BRAIN-OT\models\modbus_model.pkl"
        )

    def predict(self, packet_info):

        try:

            features = [[
                packet_info["packet_length"],
                packet_info["destination_port"] or 0,
                packet_info["source_port"] or 0,
                1 if packet_info["protocol"] == "TCP" else 0
            ]]

            prediction = self.model.predict(features)[0]

            return prediction

        except Exception as e:

            print("ML Error:", e)
            return 0