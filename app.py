import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Electricity Demand Forecasting",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Electricity Demand Forecasting")
st.write("Machine Learning based electricity demand prediction")

st.sidebar.header("Prediction Input")

temperature = st.sidebar.number_input(
    "Temperature",
    min_value=0.0,
    max_value=50.0,
    value=25.0
)

humidity = st.sidebar.number_input(
    "Humidity",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

hour = st.sidebar.slider(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)

dayofweek = st.sidebar.slider(
    "Day of Week",
    min_value=0,
    max_value=6,
    value=2
)

month = st.sidebar.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)

year = st.sidebar.number_input(
    "Year",
    min_value=2020,
    max_value=2035,
    value=2025
)

dayofyear = st.number_input(
    "Day of Year",
    min_value=1,
    max_value=366,
    value=180
)

quarter = (month - 1) // 3 + 1

if st.button("Predict Demand"):

    input_data = pd.DataFrame({
        "hour": [hour],
        "dayofweek": [dayofweek],
        "month": [month],
        "year": [year],
        "dayofyear": [dayofyear],
        "quarter": [quarter],
        "Temperature": [temperature],
        "Humidity": [humidity]
    })

    model = joblib.load("model.pkl")

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Electricity Demand: {prediction[0]:,.2f}"
    )
