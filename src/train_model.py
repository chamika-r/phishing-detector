import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

print("=" * 50)
print("PHISHING DETECTOR — MODEL TRAINING")
print("=" * 50)

# 1. Load data
print("\n[1/5] Loading dataset...")
df = pd.read_csv('data/emails.csv')
X = df.drop(columns=['Email No.', 'Prediction'])
y = df['Prediction']
print(f"      {len(df)} emails loaded.")

# 2. Split data
print("\n[2/5] Splitting into train/test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"      Train: {len(X_train)} emails")
print(f"      Test:  {len(X_test)} emails")

# 3. Train model
print("\n[3/5] Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("      Training complete.")

# 4. Evaluate
print("\n[4/5] Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"      Accuracy: {accuracy * 100:.2f}%")
print("\n" + classification_report(
    y_test, y_pred,
    target_names=['Safe', 'Phishing']
))

# 5. Save model and feature columns
print("[5/5] Saving model...")
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/phishing_model.pkl')
joblib.dump(X.columns.tolist(), 'models/feature_columns.pkl')
print("      Saved to models/phishing_model.pkl")
print("      Saved to models/feature_columns.pkl")

print("\n" + "=" * 50)
print("TRAINING COMPLETE")
print("=" * 50)