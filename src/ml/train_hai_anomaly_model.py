import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

print("===================================")
print("HAI PLC ANOMALY DETECTION TRAINING")
print("===================================")

# -----------------------------------
# DATASET PATHS
# -----------------------------------

TRAIN_FILE = r"C:\Atharva\BRAIN-OT\datasets\hai\hai-21.03\train1.csv"
TEST_FILE = r"C:\Atharva\BRAIN-OT\datasets\hai\hai-21.03\test1.csv"

# -----------------------------------
# LOAD DATA
# -----------------------------------

print("\nLoading training dataset...")

train_df = pd.read_csv(TRAIN_FILE)

print("Training Shape:", train_df.shape)

print("\nLoading testing dataset...")

test_df = pd.read_csv(TEST_FILE)

print("Testing Shape:", test_df.shape)

# -----------------------------------
# REMOVE NON-FEATURE COLUMNS
# -----------------------------------

drop_columns = [
    "time",
    "attack",
    "attack_P1",
    "attack_P2",
    "attack_P3"
]

X_train = train_df.drop(columns=drop_columns)

X_test = test_df.drop(columns=drop_columns)

y_test = test_df["attack"]

print("\nTraining Features:", X_train.shape[1])

# -----------------------------------
# TRAIN ISOLATION FOREST
# -----------------------------------

print("\nTraining Isolation Forest...")

model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42
)

model.fit(X_train)

print("Training Complete")

# -----------------------------------
# PREDICTIONS
# -----------------------------------

print("\nRunning anomaly detection...")

predictions = model.predict(X_test)

# Isolation Forest:
# 1 = normal
# -1 = anomaly

predictions = [1 if p == -1 else 0 for p in predictions]

# -----------------------------------
# EVALUATION
# -----------------------------------

print("\n===================================")
print("EVALUATION RESULTS")
print("===================================")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# -----------------------------------
# SAVE MODEL
# -----------------------------------

MODEL_PATH = r"C:\Atharva\BRAIN-OT\models\hai_anomaly_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel Saved:")
print(MODEL_PATH)