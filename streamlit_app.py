import streamlit as st
import numpy as np
import requests

st.title("Customer Churn Prediction")
st.subheader("Fill the customer details to predict churn")

# --- Collect inputs ---

# Binary features
gender = st.radio("Gender", ["Male", "Female"])
senior_citizen = st.radio("Senior Citizen", ["Yes", "No"])
partner = st.radio("Has Partner", ["Yes", "No"])
dependents = st.radio("Has Dependents", ["Yes", "No"])

# Numeric features
tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.text_input("Total Charges", "800.0")

# Categorical features
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
phone_service = st.radio("Phone Service", ["Yes", "No"])
paperless_billing = st.radio("Paperless Billing", ["Yes", "No"])

# Convert inputs to model format
def encode_input():
    binary_map = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}
    cat_map = {
        "DSL": 0, "Fiber optic": 1, "No": 2,
        "Month-to-month": 0, "One year": 1, "Two year": 2,
        "Electronic check": 0, "Mailed check": 1, "Bank transfer (automatic)": 2, "Credit card (automatic)": 3,
        "No phone service": 0, "No": 1, "Yes": 2,
        "No internet service": 0, "No": 1, "Yes": 2
    }

    features = [
        binary_map[gender],
        binary_map[senior_citizen],
        binary_map[partner],
        binary_map[dependents],
        int(tenure),
        float(monthly_charges),
        float(total_charges),

        cat_map[phone_service],
        cat_map[multiple_lines],
        cat_map[internet_service],
        cat_map[online_security],
        cat_map[online_backup],
        cat_map[device_protection],
        cat_map[tech_support],
        cat_map[streaming_tv],
        cat_map[streaming_movies],
        cat_map[contract],
        cat_map[paperless_billing],
        cat_map[payment_method],

        # Add 12 more dummy features or additional ones if in your dataset
        # Assuming you need 30 total features
    ]

    while len(features) < 30:
        features.append(0)  # Padding with 0s for now, replace with actual features

    return features

# --- Predict ---
if st.button("Predict Churn"):
    features = encode_input()
    data = {"features": features}

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            prediction = "Yes" if result["prediction"] == 1 else "No"
            st.success(f"Prediction: Customer will churn? {prediction}")
        else:
            st.error("Something went wrong with the prediction request.")
    except Exception as e:
        st.error(f"Error: {e}")

