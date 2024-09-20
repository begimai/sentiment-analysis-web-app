import matplotlib.pyplot as plt
import pandas as pd
import os


# Function to create emotion plot over the conversation
def create_emotion_conversation_plot(emotions):
    df = pd.DataFrame({'Conversation Step': range(1, len(emotions) + 1), 'Emotion': emotions})

    plt.figure(figsize=(10, 6))
    plt.plot(emotions, df['Conversation Step'], marker='o', linestyle='-', color='b')  # Swap x and y
    plt.yticks(df['Conversation Step'])  # Set y-ticks to the conversation steps
    plt.xlabel('Emotion')  # Update x-label
    plt.ylabel('Conversation Step')  # Update y-label
    plt.title('Emotions Over the Course of the Conversation')

    # Save plot as an image
    plot_path = os.path.join('static', 'emotion_conversation_plot.png')
    plt.savefig(plot_path)
    plt.close()
