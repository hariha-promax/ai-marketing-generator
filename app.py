import gradio as gr
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
API_KEY = os.environ.get("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def generate(product, audience, tone, content_type):

    prompt = f"""
    Generate a {content_type}.
    Product: {product}
    Target Audience: {audience}
    Tone: {tone}.
    Make it persuasive and creative.
    """

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]
    else:
        return "Model is loading. Try again in 20 seconds."

demo = gr.Interface(
    fn=generate,
    inputs=[
        "text",
        "text",
        "text",
        gr.Dropdown(["Social Media Post", "Email Campaign", "Product Description", "Advertisement Copy"])
    ],
    outputs="text",
    title="AI Marketing Content Generator"
)

port = int(os.environ.get("PORT", 10000))
demo.launch(server_name="0.0.0.0", server_port=port)
