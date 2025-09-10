import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set page config
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# Load model and encoders
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

loaded_model = model_data["model"]
feature_names = model_data["features_names"]

st.title("📊 Customer Churn Prediction System")

st.write("Fill in the details below to predict if a customer will churn or not.")

# Sidebar for input parameters
st.sidebar.header("Customer Information")

def user_input_features():
    gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen (0 = No, 1 = Yes)", [0, 1])
    Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
    Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.sidebar.selectbox("Online Security", ["No", "Yes", "No internet service"])
    OnlineBackup = st.sidebar.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    DeviceProtection = st.sidebar.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    TechSupport = st.sidebar.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    StreamingTV = st.sidebar.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                                             "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.sidebar.slider("Monthly Charges ($)", 18.25, 118.75, 70.0)
    TotalCharges = st.sidebar.slider("Total Charges ($)", 0.0, 8684.8, 1000.0)

    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    
    features = pd.DataFrame([data])
    return features

input_df = user_input_features()

# Encode input data
for col, encoder in encoders.items():
    input_df[col] = encoder.transform(input_df[col])

# Prediction
prediction = loaded_model.predict(input_df)[0]
prediction_prob = loaded_model.predict_proba(input_df)[0]

st.subheader("Prediction Result:")
result = "🔴 Churn" if prediction == 1 else "🟢 No Churn"
st.write(f"**Prediction:** {result}")

st.subheader("Prediction Probability:")
st.write(f"Probability of No Churn: {prediction_prob[0]:.2f}")
st.write(f"Probability of Churn: {prediction_prob[1]:.2f}")
