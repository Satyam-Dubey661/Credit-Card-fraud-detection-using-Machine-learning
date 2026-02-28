import streamlit as st
import joblib
import numpy as np

model = joblib.load("Creditcard")

st.title("Credit Card Fraud Detection")

input_data = st.text_input("Enter 29 values separated by comma")

if st.button("Predict"):
    values = list(map(float, input_data.split(",")))
    prediction = model.predict([values])

    if prediction[0] == 0:
        st.success("Normal Transaction")
    else:
        st.error("Fraud Transaction")
