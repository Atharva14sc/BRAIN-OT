import pandas as pd

df = pd.read_csv(
    r"C:\Users\athar\Downloads\Train_Test_IoT_Modbus.csv"
)

print(df["type"].value_counts())