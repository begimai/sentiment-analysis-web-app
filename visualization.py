import seaborn as sns
import matplotlib.pyplot as plt

# Function to create and save sentiment distribution plot
def create_sentiment_plot(df):
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.savefig('static/sentiment_plot.png')  # Save plot to 'static' folder
    plt.close()  # Close plot to avoid memory issues
