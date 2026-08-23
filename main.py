import streamlit as st
import pandas as pd
import joblib

model = joblib.load("svm_model1.pkl")

st.set_page_config(
    page_title="Iris flower Prediction",
    page_icon="🎗️",
    layout="wide"
)

st.title("Iris Flower Prediction",text_alignment="center")

col1 = st.columns(1)[0]

with col1:
   sepal_length = st.slider(
    "Sepal Length (cm)",
    min_value=4.3,
    max_value=7.9,
    value=5.1,
    step=0.1
)

sepal_width = st.slider(
    "Sepal Width (cm)",
    min_value=2.0,
    max_value=4.4,
    value=3.5,
    step=0.1
)

petal_length = st.slider(
    "Petal Length (cm)",
    min_value=1.0,
    max_value=6.9,
    value=1.4,
    step=0.1
)

petal_width = st.slider(
    "Petal Width (cm)",
    min_value=0.1,
    max_value=2.5,
    value=0.2,
    step=0.1
)


predict = st.button(
        "🔮 Predict Iris Flower",
        type="primary",
        use_container_width=True
    )

if predict:
   input_data = pd.DataFrame({
        "SepalLengthCm": [sepal_length],
        "SepalWidthCm": [sepal_width],
        "PetalLengthCm": [petal_length],
        "PetalWidthCm": [petal_width]
    })

   prediction = model.predict(input_data)[0]

   reverse_mapping = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }

   flower_name = reverse_mapping[prediction]
   

   st.success(f"Predicted Flower: **{flower_name.capitalize()}**")
