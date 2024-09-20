from sentiment_analysis import predict_emotions
import unittest

class TestSentimentAnalysis(unittest.TestCase):
    def test_predict_emotions(self):
        self.assertEqual(predict_emotions("I love this!"), "love")  # Replace with expected emotion
        self.assertEqual(predict_emotions("I hate it."), "anger")  # Replace with expected emotion


if __name__ == '__main__':
    unittest.main()
