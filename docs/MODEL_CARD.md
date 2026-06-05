# Model Card — Phishing Email Classifier

## Model Overview

| Property | Detail |
|----------|--------|
| Model Type | Logistic Regression |
| Task | Binary Classification |
| Input | Email word frequency vector (3,000 features) |
| Output | Label (safe/phishing) + probability scores |
| Accuracy | 97.20% |

---

## Training Data

| Property | Detail |
|----------|--------|
| Dataset | Email Spam Classification Dataset |
| Source | Kaggle (balaka18) |
| Total Emails | 5,172 |
| Safe Emails | 3,672 (71%) |
| Phishing Emails | 1,500 (29%) |
| Features | 3,000 word frequency columns |
| Format | Bag-of-words (pre-processed) |

---

## Training Configuration

| Property | Detail |
|----------|--------|
| Train/Test Split | 80% / 20% |
| Training Samples | 4,137 |
| Test Samples | 1,035 |
| Max Iterations | 1,000 |
| Random State | 42 |

---

## Performance Metrics

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Safe | 0.98 | 0.98 | 0.98 | 739 |
| Phishing | 0.94 | 0.96 | 0.95 | 296 |
| **Overall** | **0.97** | **0.97** | **0.97** | **1,035** |

---

## Limitations

- Dataset uses word frequency counts, not raw email text
- Model may struggle with new phishing tactics using uncommon words
- Not suitable as a sole security measure in production
- Trained on a specific dataset that may not represent all email types

---

## Intended Use

This model is built for **educational purposes** as part of a
cybersecurity portfolio project. It demonstrates the application
of machine learning to email security threat detection.