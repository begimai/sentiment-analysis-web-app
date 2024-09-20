from flask import Flask, request, render_template
import matplotlib.pyplot as plt
from sentiment_analysis import predict_emotions
from visualization import create_emotion_conversation_plot

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze_bulk', methods=['POST'])
def analyze_bulk():
    texts = request.form.getlist('texts')[0].splitlines()
    emotions = []
    for text in texts:
        prediction = predict_emotions(text)
        emotions.append(prediction)
    create_emotion_conversation_plot(emotions)  # Create the conversation emotion plot

    zipped_data = zip(texts, emotions)
    return render_template('bulk_result.html', zipped_data=zipped_data, plot_url='static/emotion_conversation_plot.png')


if __name__ == '__main__':
    app.run(debug=True)
