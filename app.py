import logging
import warnings
import gradio as gr
from transformers import pipeline

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.CRITICAL)

# Load model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

# Chat function
def chat_response(user_input):
    output = chatbot(
        user_input,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )
    return output[0]['generated_text']

# Gradio UI
UI = gr.Interface(
    fn=chat_response,
    inputs="text",
    outputs=gr.Textbox(lines=10),
    title="ChatBot"
)

UI.launch()
