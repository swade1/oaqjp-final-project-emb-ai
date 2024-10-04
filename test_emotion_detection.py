from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        max_key = max(result_1, key=result_1.get)
        self.assertEqual(max_key, 'joy')
    
        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        max_key = max(result_2, key=result_2.get)
        self.assertEqual(max_key, 'anger')
    
        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        max_key = max(result_3, key=result_3.get)
        self.assertEqual(max_key, 'disgust')

        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        max_key = max(result_4, key=result_4.get)
        self.assertEqual(max_key, 'sadness')

        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        max_key = max(result_5, key=result_5.get)
        self.assertEqual(max_key, 'fear')

unittest.main() 
