# 💡 Customer Churn Prediction Web App

A full-stack web application that predicts whether a customer is likely to churn based on their service usage and demographic information.

## 🚀 Demo
Try the web app here: **[🔗 Deployed URL](https://your-deployment-link.com)**  
_(Replace with your actual deployment link)_

---

## 📌 Project Overview

This project uses a machine learning model to predict customer churn. It includes:
- A **Streamlit frontend** for a user-friendly UI
- A **Flask backend** exposing a REST API
- A **trained Random Forest model**
- End-to-end deployment on a cloud platform (like Render)

---

## 🧠 Technologies Used

### 👨‍💻 Frontend:
- [Streamlit](https://streamlit.io/) – interactive UI

### 🛠️ Backend:
- [Flask](https://flask.palletsprojects.com/) – lightweight API server
- [Gunicorn](https://gunicorn.org/) – WSGI server for production

### 📊 Machine Learning:
- Scikit-learn
- Pandas / NumPy
- RandomForestClassifier
- StandardScaler

### 🔗 Deployment:
- Render (Free Hosting): https://churn-prediction-sru2.onrender.com
- GitHub for version control

---

## 📈 Model Details
- **Algorithm:** Random Forest Classifier
- **Input Features:** 30 customer attributes (binary, numeric, and categorical)
- **Preprocessing:** StandardScaler for normalization

---

## 🧪 How It Works

1. **Streamlit Frontend:** Collects customer inputs
2. **Flask API:** Accepts features and returns prediction
3. **ML Model:** Processes input & outputs churn status
4. **User Feedback:** Displays "Will Churn" or "Won’t Churn"

---

