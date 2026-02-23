import gradio as gr
from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate(product, audience, tone, content_type):
    prompt = f"""
    Generate a {content_type}.
    Product: {product}
    Target Audience: {audience}
    Tone: {tone}.
    Make it persuasive and creative.
    """
    result = generator(prompt, max_length=150)
    return result[0]["generated_text"]

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

import os
port = int(os.environ.get("PORT", 10000))
demo.launch(server_name="0.0.0.0", server_port=port)
