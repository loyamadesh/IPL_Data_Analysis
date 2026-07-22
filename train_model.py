import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

print("Loading dataset...")
df = pd.read_excel("ipl.xlsx")

# Create match-level data
matches = df.groupby("match_id").first().reset_index()

# Remove rows without winner
matches = matches.dropna(subset=["match_won_by"])

features = ["batting_team", "bowling_team", "toss_winner", "venue"]
features = [col for col in features if col in matches.columns]

X = matches[features]
y = matches["match_won_by"]

# Encode categorical data
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Improved Model Accuracy: {accuracy:.2f}")

os.makedirs("models", exist_ok=True)

with open("models/match_predictor.pkl", "wb") as f:
    pickle.dump((model, encoders, target_encoder), f)

print("Improved model saved successfully!")