import sys
import os
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(os.path.join(SRC_DIR, "ml"))

from plc_simulator import PLCSimulator
from ml_engine import MLEngine

plc = PLCSimulator()

ml_engine = MLEngine()

while True:

    data = plc.generate_normal_data()

    threat = ml_engine.classify_modbus(
        data["FC1_Read_Input_Register"],
        data["FC2_Read_Discrete_Value"],
        data["FC3_Read_Holding_Register"],
        data["FC4_Read_Coil"]
    )

    print("\nPLC DATA")
    print(data)

    print("ML THREAT TYPE :", threat)

    time.sleep(2)