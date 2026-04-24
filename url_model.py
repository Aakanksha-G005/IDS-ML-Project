import pandas as pd

# Load dataset
df = pd.read_csv("urls.csv")

# Feature extraction
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('/'),
        url.count('-')
    ]

# Create X and y
X = df['url'].apply(extract_features).tolist()
y = df['label']

# ML part
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test new URL
test_url = "http://free-gift-card.xyz"
features = extract_features(test_url)
prediction = model.predict([features])

if prediction[0] == 1:
    print("🚨 Malicious URL")
else:
    print("✅ Safe URL")