import streamlit as st
import requests
import os

st.title("AutoContent Generator")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
API_KEY = st.secrets["HF_TOKEN"]

headers = {"Authorization": f"Bearer {API_KEY}"}

product = st.text_input("Product Name")
audience = st.text_input("Target Audience")
tone = st.text_input("Tone")
content_type = st.selectbox(
    "Content Type",
    ["Social Media Post", "Email Campaign", "Product Description", "Advertisement Copy"]
)

if st.button("Generate Content"):
    prompt = f"""
    Generate a {content_type}.
    Product: {product}
    Target Audience: {audience}
    Tone: {tone}.
    Make it persuasive and creative.
    """

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    result = response.json()

    if isinstance(result, list):
        st.success(result[0]["generated_text"])
    else:
        st.error("Model loading. Try again.")
