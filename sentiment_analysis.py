from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline('sentiment-analysis')

# Function to analyze sentiment of a single text
def analyze_sentiment(text):
    return sentiment_pipeline(text)[0]  # Returns a dictionary with 'label' and 'score'
