import pandas as pd

DATASET = r"C:\Atharva\BRAIN-OT\datasets\hai\hai-21.03\train1.csv"

print("Loading Dataset...")

df = pd.read_csv(DATASET)

print("\nShape:")
print(df.shape)

print("\nAttack Distribution:")
print(df["attack"].value_counts())

print("\nAttack Percentage:")
print(df["attack"].value_counts(normalize=True) * 100)