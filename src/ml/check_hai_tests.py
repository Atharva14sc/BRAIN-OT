import pandas as pd

base = r"C:\Atharva\BRAIN-OT\datasets\hai\hai-21.03"

for file in [
    "test1.csv",
    "test2.csv",
    "test3.csv",
    "test4.csv",
    "test5.csv"
]:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(f"{base}\\{file}")

    print("Shape:", df.shape)

    print(df["attack"].value_counts())