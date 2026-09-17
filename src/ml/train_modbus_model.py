import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("Loading TON_IoT Modbus Dataset...")

# Dataset path
DATASET_PATH = r"C:\Users\athar\Downloads\Train_Test_IoT_Modbus.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded")
print("Shape:", df.shape)

# ----------------------------------
# Features
# ----------------------------------

X = df[
    [
        "FC1_Read_Input_Register",
        "FC2_Read_Discrete_Value",
        "FC3_Read_Holding_Register",
        "FC4_Read_Coil"
    ]
]

# ----------------------------------
# Target
# ----------------------------------

y = df["label"]

# ----------------------------------
# Split Dataset
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ----------------------------------
# Train Model
# ----------------------------------

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complete")

# ----------------------------------
# Predictions
# ----------------------------------

predictions = model.predict(X_test)

# ----------------------------------
# Evaluation
# ----------------------------------

accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("MODEL ACCURACY")
print("==============================")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

# ----------------------------------
# Save Model
# ----------------------------------

MODEL_PATH = r"C:\Atharva\BRAIN-OT\models\modbus_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel Saved To:")
print(MODEL_PATH)