## Sentiment and Emotion Analysis Web App
This web application analyzes emotions in conversational text using a pre-trained emotion classification model. Built with Flask and the Transformers library, the app allows users to input multiple lines of text and visualize the emotional responses throughout the conversation.


## Features
- **Emotion Prediction**: Classifies emotions from user-provided text based on the GoEmotions dataset.
- **Bulk Analysis**: Allows analysis of multiple lines of text simultaneously.
- **Visualization**: Displays a plot of emotions over the course of the conversation.
- **User-Friendly Interface**: Simple and intuitive web interface for input and results.


## Getting Started

### Prerequisites
- Python
- Flask
- PyTorch
- Transformers
- Matplotlib
- Pandas
- HTML/CSS

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-web-app.git
2. Navigate into the project directory:
   ```bash
   cd flask-sentiment-analyzer
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### Usage
1. Run the Flask application:
   ```bash
   python app.py
2. Open your web browser and go to http://127.0.0.1:5000/.
