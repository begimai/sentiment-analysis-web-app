import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Load tokenizer and model for GoEmotions
tokenizer = AutoTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
model = AutoModelForSequenceClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")

# Emotions associated with the model
emotion_labels = ["admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion",
                  "curiosity", "desire", "disappointment", "disapproval", "disgust", "embarrassment",
                  "excitement", "fear", "gratitude", "grief", "joy", "love", "nervousness", "optimism",
                  "pride", "realization", "relief", "remorse", "sadness", "surprise", "neutral"]


def predict_emotions(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    highest_probs = torch.topk(probs, 1)  # Get the highest probability emotion
    emotion_index = highest_probs.indices[0].item()
    return emotion_labels[emotion_index]
