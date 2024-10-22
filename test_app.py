import unittest
from application import application  # Adjust the import based on your app's filename
import json

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_fake(self):
        fake_inputs = [
            "The moon is made of hamsters",
            "Sleep is not important"
        ]

        for input in fake_inputs:
            response = self.app.post('/predict', data={'input_text': input})
            # Verify if request was successful -> Status Code = 200
            self.assertEqual(response.status_code, 200)
            
            # Check result of prediction
            prediction = json.loads(response.data)
            self.assertIn('prediction', prediction)
            self.assertEqual(prediction['prediction'], 'FAKE')

    def test_real(self):
        real_inputs = [
            "Bunnies make me happy", 
            "UofT makes students stressed"
        ]

        for input in real_inputs:
            response = self.app.post('/predict', data={'input_text': input})

            # Verify if request was successful -> Status Code = 200
            self.assertEqual(response.status_code, 200)

            # Check result of prediction
            prediction = json.loads(response.data)
            self.assertIn('prediction', prediction)
            self.assertEqual(prediction['prediction'], 'REAL')

if __name__ == '__main__':
    unittest.main()
