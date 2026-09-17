import joblib
import os
import pandas as pd


class MLEngine:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        self.modbus_model = joblib.load(
            os.path.join(
                base_dir,
                "models",
                "modbus_threat_classifier.pkl"
            )
        )

        self.label_encoder = joblib.load(
            os.path.join(
                base_dir,
                "models",
                "modbus_label_encoder.pkl"
            )
        )

        print("ML Engine Loaded")


    def classify_modbus(
        self,
        fc1,
        fc2,
        fc3,
        fc4
    ):

        sample = pd.DataFrame([{
            "FC1_Read_Input_Register": fc1,
            "FC2_Read_Discrete_Value": fc2,
            "FC3_Read_Holding_Register": fc3,
            "FC4_Read_Coil": fc4
        }])

        prediction = self.modbus_model.predict(sample)[0]

        threat_type = self.label_encoder.inverse_transform(
            [prediction]
        )[0]

        return threat_type