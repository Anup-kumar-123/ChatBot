# AI Chatbot (Gradio + Transformers)

This is a simple AI chatbot built using Hugging Face Transformers and Gradio, deployed on Railway.

## Features
- Text-based chatbot
- Uses pre-trained language model (GPT-style)
- Simple web interface with Gradio
- Easy deployment

## Tech Stack
- Python
- Gradio
- Transformers
- PyTorch

## Installation (Local)

1. Clone the repo:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install dependencies:
pip install -r requirements.txt

3. Run:
python app.py

## Deployment (Railway)

1. Push code to GitHub
2. Go to Railway
3. New Project → Deploy from GitHub repo
4. Select your repo
5. Add start command:
python app.py

## Important

Make sure your app uses PORT:

import os
port = int(os.environ.get("PORT", 7860))

## Project Structure

app.py  
requirements.txt  
Procfile (optional)  
README.md  

## Model
GPT-2 / DialoGPT

## License
Free to use
