from flask import Flask, request, render_template
from sentiment_analysis import analyze_sentiment  # Sentiment analysis logic
from visualization import create_sentiment_plot  # Visualization logic
import pandas as pd

app = Flask(__name__)


# Route for homepage with input form
@app.route('/')
def index():
    return render_template('index.html')


# Route for single text analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']  # Get input text
    sentiment = analyze_sentiment(text)  # Analyze sentiment

    # Create a DataFrame to store this one result for plotting
    df = pd.DataFrame({'text': [text], 'sentiment': [sentiment['label']]})

    # Generate plot and save it
    create_sentiment_plot(df)

    return render_template('result.html', text=text, sentiment=sentiment, plot_url='static/sentiment_plot.png')


# Route for bulk analysis
@app.route('/analyze_bulk', methods=['POST'])
def analyze_bulk():
    texts = request.form['texts'].strip().split("\n")
    sentiments = [analyze_sentiment(text.strip())['label'] for text in texts]

    # Create a list of dictionaries for the template
    results = [{'text': text, 'sentiment': sentiment} for text, sentiment in zip(texts, sentiments)]

    df = pd.DataFrame({'text': texts, 'sentiment': sentiments})
    create_sentiment_plot(df)

    return render_template('bulk_result.html', results=results, plot_url='static/sentiment_plot.png')


if __name__ == '__main__':
    app.run(debug=True)
