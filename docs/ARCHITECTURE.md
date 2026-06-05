# System Architecture

## Overview
The Phishing Detector is a two-component system: an offline training pipeline
that builds the ML model, and a live REST API that serves predictions.

---

## Data Flow
Raw Email Text
│
▼
Word Frequency Extraction
(count occurrences of 3,000 known words)
│
▼
Logistic Regression Model
(trained on 5,172 real emails)
│
▼
Prediction + Confidence Score
│
▼
Rule-Based Explanation Engine
(flags known suspicious words)
│
▼
JSON Response to Client
---

## Components

### 1. Training Pipeline (`src/train_model.py`)
- Loads `data/emails.csv`
- Splits data 80/20 into train and test sets
- Trains a Logistic Regression classifier
- Evaluates on test set
- Saves model to `models/phishing_model.pkl`
- Saves feature columns to `models/feature_columns.pkl`

### 2. REST API (`src/app.py`)
- Built with Flask
- Loads the saved model on startup
- Accepts raw email text via POST request
- Extracts word frequency features from input
- Returns prediction, confidence, and explanation

### 3. Explanation Engine (inside `src/app.py`)
- Rule-based — no external API needed
- Matches email words against a list of known phishing indicators
- Returns a human-readable explanation of the prediction

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.9 |
| ML Model | scikit-learn Logistic Regression |
| API Framework | Flask |
| Data Processing | pandas |
| Model Storage | joblib |

---

## File Structure

phishing-detector/
├── src/
│   ├── app.py               # Flask API + explanation engine
│   ├── train_model.py       # Training pipeline
│   └── explore_data.py      # Data exploration
├── data/
│   └── emails.csv           # 5,172 labeled emails
├── models/
│   ├── phishing_model.pkl   # Serialized trained model
│   └── feature_columns.pkl  # Feature column names
└── docs/
├── ARCHITECTURE.md      # This file
└── MODEL_CARD.md        # Model details and metrics

