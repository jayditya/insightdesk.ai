import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Correct relative paths
with open('../ml_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('../ml_model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)[0]
    return jsonify({'response': prediction})

if __name__ == '__main__':
    app.run(debug=True)
