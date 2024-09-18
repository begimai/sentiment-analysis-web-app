from sentiment_analysis import analyze_sentiment
import unittest

class TestSentimentAnalysis(unittest.TestCase):
    def test_analyze_sentiment(self):
        # Define test input and expected output
        test_text = "I love this product! It's amazing."
        expected_label = "POSITIVE"
        expected_score = 0.999

        # Call the function to test
        result = analyze_sentiment(test_text)

        # Print the result (Optional: only for debugging purposes)
        print(f"Text: {test_text}")
        print(f"Sentiment: {result['label']} (Confidence: {result['score']:.4f})")

        # Assertions to verify the function's output
        self.assertEqual(result['label'], expected_label, "Label does not match the expected value.")
        self.assertAlmostEqual(result['score'], expected_score, places=2, msg="Score does not match the expected value.")

if __name__ == '__main__':
    unittest.main()
