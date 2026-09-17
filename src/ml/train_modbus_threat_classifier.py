import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

print("===================================")
print("TON_IOT THREAT CLASSIFIER TRAINING")
print("===================================")

# -----------------------------------
# LOAD DATASET
# -----------------------------------

DATASET = r"C:\Users\athar\Downloads\Train_Test_IoT_Modbus.csv"

print("\nLoading Dataset...")

df = pd.read_csv(DATASET)

print("Shape:", df.shape)

# -----------------------------------
# FEATURES
# -----------------------------------

X = df[
    [
        "FC1_Read_Input_Register",
        "FC2_Read_Discrete_Value",
        "FC3_Read_Holding_Register",
        "FC4_Read_Coil"
    ]
]

# -----------------------------------
# TARGET
# -----------------------------------

y = df["type"]

# -----------------------------------
# ENCODE LABELS
# -----------------------------------

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print("\nThreat Classes:")

for index, name in enumerate(encoder.classes_):
    print(index, "->", name)

# -----------------------------------
# TRAIN TEST SPLIT
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# -----------------------------------
# MODEL
# -----------------------------------

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("Training Complete")

# -----------------------------------
# EVALUATION
# -----------------------------------

predictions = model.predict(X_test)

print("\n==============================")
print("MODEL ACCURACY")
print("==============================")

print(
    "Accuracy:",
    round(accuracy_score(y_test, predictions) * 100, 2),
    "%"
)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_
    )
)

print("\nConfusion Matrix")

print(confusion_matrix(y_test, predictions))

# -----------------------------------
# SAVE MODEL
# -----------------------------------

MODEL_PATH = r"C:\Atharva\BRAIN-OT\models\modbus_threat_classifier.pkl"

ENCODER_PATH = r"C:\Atharva\BRAIN-OT\models\modbus_label_encoder.pkl"

joblib.dump(model, MODEL_PATH)

joblib.dump(encoder, ENCODER_PATH)

print("\nSaved Model:")
print(MODEL_PATH)

print("\nSaved Encoder:")
print(ENCODER_PATH)