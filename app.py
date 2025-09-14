import streamlit as st
import pandas as pd
import joblib
import os
BASE_DIR = os.path.dirname(__file__)  
model_path = os.path.join(BASE_DIR, "pipe.pkl")

with open(model_path, "rb") as f:
    model = joblib.load(f)

st.set_page_config(page_title="Income Prediction App", layout="centered")
st.title("Income Prediction")
st.write("Fill in the details below and the model will predict the income category.")

 
age = st.number_input("Age", min_value=18, max_value=100, value=30)
hours_per_week = st.number_input("Hours per week", min_value=1, max_value=100, value=40)

workclass = st.selectbox("Workclass", [
    "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
    "Local-gov", "State-gov", "Without-pay", "Never-worked"
])

education = st.selectbox("Education", [
    "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school",
    "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th",
    "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"
])

marital_status = st.selectbox("Marital Status", [
    "Married-civ-spouse", "Divorced", "Never-married",
    "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"
])

occupation = st.selectbox("Occupation", [
    "Tech-support", "Craft-repair", "Other-service", "Sales",
    "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
    "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
    "Transport-moving", "Priv-house-serv", "Protective-serv",
    "Armed-Forces"
])

relationship = st.selectbox("Relationship", [
    "Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"
])

race = st.selectbox("Race", [
    "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"
])

sex = st.selectbox("Sex", ["Male", "Female"])

native_country = st.selectbox("Native Country", [
    "United-States", "Cambodia", "England", "Puerto-Rico", "Canada",
    "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece",
    "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy",
    "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland",
    "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti",
    "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland",
    "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru",
    "Hong", "Holand-Netherlands"
])


raw_input = pd.DataFrame([{
    "age": age,
    "workclass": workclass,
    "education": education,
    "marital_status": marital_status,
    "occupation": occupation,
    "relationship": relationship,
    "race": race,
    "sex": sex,
    "hours_per_week": hours_per_week,
    "native_country": native_country
}])


if st.button("Predict Income"):
    prediction = model.predict(raw_input)[0]
    if prediction == "<=50K":
        st.success("💰 Predicted Income: Salary will be **50,000 or less**.")
    else:
        st.success("💰 Predicted Income: Salary will be **greater than 50,000**.")
