import os
import gdown
from flask import Flask, request, jsonify
import joblib
import numpy as np

# ✅ Check if model file exists, if not, download
if not os.path.exists('churn_model_rf.pkl'):
    print("Downloading churn_model_rf.pkl...")
    gdown.download('https://drive.google.com/uc?id=1HgESyzQNwkTnM65kfiF6wLLNgyBJ-7GP', 'churn_model_rf.pkl', quiet=False)

# ✅ Check if scaler file exists, if not, download
if not os.path.exists('scaler.pkl'):
    print("Downloading scaler.pkl...")
    gdown.download('https://drive.google.com/uc?id=1Ql41eIzIFYDW4cV7Oh5fpZzZfimAe3-o', 'scaler.pkl', quiet=False)
# Now safe to load
model = joblib.load('churn_model_rf.pkl')
scaler = joblib.load('scaler.pkl')

# Load model and scaler
model = joblib.load('churn_model_rf.pkl')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)

# ✅ Add this to avoid 404 on homepage
@app.route('/')
def home():
    return "🎯 Customer Churn Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        print("Received data:", data)
        input_data = np.array(data['features']).reshape(1, -1)
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

