import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_pipeline.pkl")

st.title("Vehicle Maintenance Cost Predictor")

brand = st.selectbox("Brand", ["Ford", "Tata", "Hyundai"])
model_name = st.text_input("Model")
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
age = st.number_input("Vehicle Age (Years)", min_value=0)
km_driven = st.number_input("Kilometers Driven", min_value=0)
num_services = st.number_input("Number of Services", min_value=0)
behavior = st.selectbox("Driving Behavior", ["Careful", "Normal", "Aggressive"])

if st.button("Predict Maintenance Cost"):
    input_data = pd.DataFrame([{
        "Brand": brand,
        "Model": model_name,
        "FuelType": fuel,
        "Transmission": transmission,
        "AgeYears": age,
        "KilometersDriven": km_driven,
        "NumServices": num_services,
        "DrivingBehavior": behavior
    }])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Annual Maintenance Cost: INR {int(prediction)}")
