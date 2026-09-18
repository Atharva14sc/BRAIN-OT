import random
import time


class PLCSimulator:

    def generate_normal_data(self):

        return {
            "FC1_Read_Input_Register": random.randint(0, 10),
            "FC2_Read_Discrete_Value": random.randint(0, 10),
            "FC3_Read_Holding_Register": random.randint(0, 10),
            "FC4_Read_Coil": random.randint(0, 10)
        }


if __name__ == "__main__":

    plc = PLCSimulator()

    while True:

        data = plc.generate_normal_data()

        print(data)

        time.sleep(2)