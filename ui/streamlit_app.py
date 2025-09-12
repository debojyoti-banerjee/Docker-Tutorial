import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from app.predictor import predictor
from app.trainer import trainer

st.title("Iris Predictor App")

if st.button("Train model"):
    trainer=trainer()
    trainer.train_and_save()
    st.success("Model retrained and save")

st.header("Make a Prediction")

sepal_length=st.text_input("Sepal-Length")
sepal_width=st.text_input("Sepal-Width")
petal_length=st.text_input("Petal-Length")
petal_width=st.text_input("Petal-Width")

if st.button("Predict"):
    try:
        prediction=predictor()
        features=[sepal_length,sepal_width,petal_length,petal_width]
        result=prediction.predict(features)
        st.success(f"Predicted class is {result}")
    except Exception as e:
        print(str(e))
        st.error("Some Error occured")