from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# -----------------------------
# STEP 1: LOAD DATASET
# -----------------------------
df = pd.read_csv("final_dataset.csv")

print("Dataset Loaded:")
print(df.head())

# -----------------------------
# STEP 2: SPLIT FEATURES & LABEL
# -----------------------------
X = df[['Time', 'Protocol', 'Length', 'Time_diff', 'Packet_rate']]
y = df['Label']

# -----------------------------
# STEP 3: TRAIN-TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# -----------------------------
# MODEL COMPARISON
# -----------------------------

models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000)
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"{name} Accuracy: {acc}")

# -----------------------------
# STEP 4: TRAIN MODEL
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# STEP 5: PREDICTIONS
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# STEP 6: EVALUATION
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# STEP 7: SAVE MODEL
# -----------------------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ Model trained and saved as model.pkl")
# -----------------------------
# CONFUSION MATRIX DISPLAY
# -----------------------------
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix")
plt.show()
# FEATURE IMPORTANCE GRAPH
features = ['Time', 'Protocol', 'Length', 'Time_diff', 'Packet_rate']
importances = model.feature_importances_

import matplotlib.pyplot as plt

plt.figure()
plt.barh(features, importances)
plt.xlabel("Importance")
plt.title("Feature Importance")
plt.show()

import matplotlib.pyplot as plt

names = list(results.keys())
values = list(results.values())

plt.figure()
plt.bar(names, values)
plt.title("Model Comparison")
plt.ylabel("Accuracy")
plt.xlabel("Models")
plt.show()
