import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from app.trainer import trainer
import requests

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
        features=[sepal_length,sepal_width,petal_length,petal_width]
        response=requests.post("http://localhost:5000/predict",json={"features":features},timeout=5)
        if response.status_code==200:
            result=response.json()["prediction"]
            st.success(f"Predicted class : {result}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        print(str(e))
        st.error(f"Request failed: {e}")