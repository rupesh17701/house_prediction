import streamlit as st
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("house_model.pkl")
columns = joblib.load("columns.pkl")

st.title("🏠 House Price Prediction")

# Inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

# Encode inputs
input_dict = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
    "mainroad_yes": 1 if mainroad == "yes" else 0,
    "guestroom_yes": 1 if guestroom == "yes" else 0,
    "basement_yes": 1 if basement == "yes" else 0,
    "hotwaterheating_yes": 1 if hotwaterheating == "yes" else 0,
    "airconditioning_yes": 1 if airconditioning == "yes" else 0,
    "prefarea_yes": 1 if prefarea == "yes" else 0,
}

# Convert to dataframe
input_df = pd.DataFrame([input_dict])

# Match training columns
input_df = input_df.reindex(columns=columns, fill_value=0)

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")

