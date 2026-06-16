import streamlit as st
import pandas as pd
import joblib

model = joblib.load("customer_churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")

st.write("Predict whether a customer is likely to churn.")
