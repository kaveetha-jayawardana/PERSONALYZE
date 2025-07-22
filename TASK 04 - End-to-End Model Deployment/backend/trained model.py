# backend/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
import os

# Load dataset
df = pd.read_csv(r"C:\Users\kaveethaj\Downloads\BlueChip Documents\TASK 04 - End-to-End Model Deployment\personality_dataset.csv")

# Handle missing values
df.dropna(inplace=True)

# Encode categorical
df = df.replace({'Yes': 1, 'No': 0, 'Introvert': 0, 'Extrovert': 1}).infer_objects()

# Features & target
X = df.drop('Personality', axis=1)
y = df['Personality']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = SVC()
model.fit(X_train_scaled, y_train)

# Save model
os.makedirs("backend/model", exist_ok=True)
joblib.dump(model, "backend/model/personality_model.pkl")
joblib.dump(scaler, "backend/model/scaler.pkl")

print("✅ Model and scaler saved successfully!")
