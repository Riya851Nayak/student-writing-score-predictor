import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/writing_score_model.pkl")
st.title("student Writing Score predictor")
##st.write("Enter student score to predict writing score")

math_score =st.number_input("math score",min_value=0,max_value=100,value=70)
reading_score =st.number_input("reading score",min_value=0,max_value=100,value=75)

if st.button("Predict writing score"):
    input_data =pd.DataFrame([[math_score,reading_score]],columns=["math_score","reading_score"])
    prediction = model.predict(input_data)
    st.success(f"predicted writing score is {prediction[0]:.2f}")