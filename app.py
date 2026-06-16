import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")

st.markdown(
"""
Predict whether a customer is likely to leave the bank.
"""
)

# Sidebar
st.sidebar.header("Customer Information")

credit_score = st.sidebar.slider("Credit Score", 350, 850, 650)
age = st.sidebar.slider("Age", 18, 92, 40)
tenure = st.sidebar.slider("Tenure", 0, 10, 5)

balance = st.sidebar.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_products = st.sidebar.selectbox(
    "Number of Products",
    [1, 2, 3, 4]
)

has_card = st.sidebar.selectbox(
    "Has Credit Card",
    [0, 1]
)

active_member = st.sidebar.selectbox(
    "Is Active Member",
    [0, 1]
)

salary = st.sidebar.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=100000.0
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

geography = st.sidebar.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

# Encoding

gender = 1 if gender == "Female" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# Prediction

if st.button("Predict Churn"):

    input_df = pd.DataFrame({
        'CreditScore':[credit_score],
        'Gender':[gender],
        'Age':[age],
        'Tenure':[tenure],
        'Balance':[balance],
        'NumOfProducts':[num_products],
        'HasCrCard':[has_card],
        'IsActiveMember':[active_member],
        'EstimatedSalary':[salary],
        'Geography_Germany':[geo_germany],
        'Geography_Spain':[geo_spain]
    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ Customer Likely To Churn")
    else:
        st.success("✅ Customer Likely To Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )
