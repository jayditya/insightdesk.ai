import os
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model and vectorizer from ../ml_model/
model_path = os.path.join(os.path.dirname(__file__), '../ml_model/model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../ml_model/vectorizer.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')
    if not message:
        return jsonify({'response': 'No message received.'}), 400

    vec_message = vectorizer.transform([message])
    prediction = model.predict(vec_message)[0]

    return jsonify({'response': prediction})

if __name__ == '__main__':
    app.run(debug=True)
