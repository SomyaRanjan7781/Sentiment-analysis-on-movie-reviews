import gradio as gr
from transformers import pipeline

# Load Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']
    
    # Format the label
    sentiment = "Positive" if label == "POSITIVE" else "Negative"
    return f"{sentiment} ({score:.2f})"

# Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter movie review text here...", label="Text"),
    outputs=gr.Textbox(label="Sentiment"),
    title="🎬 Movie Review Sentiment Analysis",
    description="Enter a movie review or sentence to classify its sentiment as Positive or Negative."
)

if __name__ == "__main__":
    iface.launch()
