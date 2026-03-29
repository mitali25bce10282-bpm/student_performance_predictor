import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Inputs and output
X = data[["study_hours", "sleep_hours", "attendance"]]
y = data["marks"]

# Train model
model = LinearRegression()
model.fit(X, y)

# UI
st.title("🎓 Student Performance Predictor")

st.write("Enter student details to predict marks")

study = st.number_input("Study Hours", min_value=0.0)
sleep = st.number_input("Sleep Hours", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    prediction = model.predict([[study, sleep, attendance]])
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
    