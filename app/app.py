import streamlit as st
import joblib

model = joblib.load("../models/sentiment_model.pkl")

st.title("Amazon Review Sentiment Analyzer")

user_input = st.text_area("Enter a review")

if st.button("Predict"):
    prediction = model.predict([user_input])[0]
    
    if prediction == 1:
        st.success("Positive Review 😊")
    else:
        st.error("Negative Review 😞")
