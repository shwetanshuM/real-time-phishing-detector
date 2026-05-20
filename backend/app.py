from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

from feature_extractor import extract_features

app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data['url']

    features = extract_features(url)

    features = np.array(features).reshape(1, -1)

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    result = "Legitimate" if prediction == 1 else "Phishing"

    confidence = float(max(probability))

    return jsonify({
        'prediction': result,
        'confidence': confidence
    })


if __name__ == '__main__':
    app.run(debug=True)