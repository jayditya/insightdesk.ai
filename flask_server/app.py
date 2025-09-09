# File: flask_server/app.py

import joblib
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# --- Define User-Friendly AI Responses ---
RESPONSE_MAP = {
    "password_reset": "To reset your password, please go to the 'Account Settings' page and click 'Reset Password'.",
    "business_hours": "Our business hours are 9 AM to 5 PM, Monday through Friday.",
    "pricing": "You can find all pricing details on our website at insightdesk.ai/pricing.",
    "billing": "For all billing issues, please email our support team at billing@insightdesk.ai."
}
DEFAULT_RESPONSE = "Thank you for your query. A support agent will get back to you shortly."

# --- Load the Trained Model and Vectorizer ---
# This path logic works by going UP one level ('..') from 'flask_server'
# and then DOWN into 'ml_model'.
try:
    model_path = os.path.join(os.path.dirname(__file__), '..', 'ml_model', 'insight_model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'ml_model', 'vectorizer.pkl')
    
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("✅ Model and vectorizer loaded successfully!")
except FileNotFoundError:
    print("❌ ERROR: Model files not found. Please run the 'train_model.py' script first!")
    model = None
    vectorizer = None

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return jsonify({'response': 'Error: Model is not loaded on the server.'}), 500

    data = request.get_json()
    message = data.get('message', '').strip()

    if not message:
        return jsonify({'response': 'Error: Please provide a message.'}), 400

    vector = vectorizer.transform([message])
    predicted_category = model.predict(vector)[0]
    ai_response = RESPONSE_MAP.get(predicted_category, DEFAULT_RESPONSE)
    
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)