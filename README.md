# Phishing Email Detector

A machine learning model trained on 5,172 real emails that detects phishing attempts with **97.20% accuracy**. Includes a REST API that analyzes any email and returns a prediction with confidence score and plain-English explanation.

---

# Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 97.20% |
| Safe Email Precision | 98% |
| Phishing Precision | 94% |
| Test Set Size | 1,035 emails |

---

# Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/chamika-r/phishing-detector.git
cd phishing-detector
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Train the model**
```bash
python src/train_model.py
```

**4. Start the API**
```bash
python src/app.py
```

API runs at `http://127.0.0.1:5000`

---

# API Endpoints

# `GET /health`
Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "model": "loaded",
  "features": 3000
}
```

---

# `POST /analyze`
Analyze an email for phishing.

**Request:**
```json
{
  "email_text": "Congratulations! You won a free prize. Click here now."
}
```

**Response:**
```json
{
  "prediction": "phishing",
  "confidence": 91.83,
  "phishing_probability": 91.83,
  "safe_probability": 8.17,
  "explanation": "This email is likely phishing. It contains 3 suspicious word(s): free, prize, click. These are common tactics used in phishing attacks."
}
```

---

# Project Structure
phishing-detector/
├── src/
│   ├── app.py            # Flask REST API
│   ├── train_model.py    # Model training script
│   └── explore_data.py   # Data exploration script
├── data/
│   └── emails.csv        # Dataset (5,172 emails)
├── models/
│   ├── phishing_model.pkl    # Trained model
│   └── feature_columns.pkl  # Feature column names
├── docs/
│   ├── ARCHITECTURE.md   # System architecture
│   └── MODEL_CARD.md     # Model details
├── requirements.txt
└── README.md

---

# How It Works

1. **Dataset** — 5,172 real emails pre-processed into word frequency counts (bag-of-words format)
2. **Model** — Logistic Regression classifier trained on 4,137 emails, tested on 1,035
3. **API** — Flask REST API loads the trained model and accepts raw email text
4. **Prediction** — Word frequencies extracted from input email, fed to model, returns label + confidence
5. **Explanation** — Rule-based engine flags specific suspicious words found in the email

---

# Tech Stack

- **Python 3.9**
- **scikit-learn** — Logistic Regression model
- **Flask** — REST API framework
- **pandas** — Data loading and processing
- **joblib** — Model serialization

---

# Dataset

- **Source:** [Email Spam Classification Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) via Kaggle
- **Size:** 5,172 emails
- **Features:** 3,000 word frequency columns
- **Labels:** 0 = Safe (3,672), 1 = Phishing (1,500)

---

# Disclaimer

This tool is built for educational purposes as part of a cybersecurity portfolio. Do not use as a sole security measure in production environments.

---

# Author

**Chamika Ranaweera**  
Undergraduate — Cybersecurity  
[GitHub](https://github.com/chamika-r)