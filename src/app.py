import warnings
warnings.filterwarnings('ignore')

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and feature columns
print("Loading model...")
model = joblib.load('models/phishing_model.pkl')
feature_columns = joblib.load('models/feature_columns.pkl')
print(f"Model loaded. {len(feature_columns)} features ready.")

def generate_explanation(prediction, phishing_prob, email_text):
    """Rule-based explanation — no paid API needed."""
    suspicious_words = [
        'free', 'win', 'winner', 'prize', 'click', 'buy', 'cheap',
        'money', 'online', 'offer', 'limited', 'viagra', 'pills',
        'casino', 'guaranteed', 'discount', 'password', 'verify',
        'urgent', 'congratulations', 'selected', 'account', 'login'
    ]
    found = [w for w in suspicious_words if w in email_text.lower().split()]

    if prediction == "phishing":
        if found:
            return (
                f"This email is likely phishing. "
                f"It contains {len(found)} suspicious word(s): "
                f"{', '.join(found[:5])}. "
                f"These are common tactics used in phishing attacks."
            )
        else:
            return (
                "This email shows phishing patterns based on its "
                "overall word frequency profile, even without "
                "obvious trigger words. Treat with caution."
            )
    else:
        return (
            "This email appears safe. It does not contain common "
            "phishing indicators and its language matches "
            "legitimate email communication."
        )

@app.route('/')
def home():
    return jsonify({
        "name": "Phishing Detector API",
        "version": "1.0.0",
        "model_accuracy": "97.20%",
        "endpoints": {
            "GET  /health": "Check API status",
            "POST /analyze": "Analyze an email"
        }
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "model": "loaded",
        "features": len(feature_columns)
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'email_text' not in data:
        return jsonify({
            "error": "Missing required field: email_text"
        }), 400

    if not data['email_text'].strip():
        return jsonify({
            "error": "email_text cannot be empty"
        }), 400

    email_text = data['email_text'].lower()

    # Count word frequencies
    word_counts = {
        word: email_text.split().count(word)
        for word in feature_columns
    }

    # Make prediction
    input_df = pd.DataFrame([word_counts])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    prediction_label = "phishing" if prediction == 1 else "safe"
    phishing_prob = round(float(probability[1]) * 100, 2)
    safe_prob = round(float(probability[0]) * 100, 2)
    confidence = round(float(max(probability)) * 100, 2)

    explanation = generate_explanation(
        prediction_label, phishing_prob, email_text
    )

    return jsonify({
        "prediction": prediction_label,
        "confidence": confidence,
        "phishing_probability": phishing_prob,
        "safe_probability": safe_prob,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)