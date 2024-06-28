
from django.test import TestCase, Client
import requests
import json

class NumberClassifierTestCase(TestCase):
    
    def test_list_cls(self):
        """
        Tests that the `/api/number-classifier/list_models/` endpoint returns a successful response (200 status code) and validates the expected structure of the response data:
        - Presence of 'success' and 'result' keys in the top-level response.
        - Presence of a 'models' key within the 'result' section.
        - Confirmation that 'models' is a list.
        
        """
        response = requests.get("http://127.0.0.1:8000/api/number-classifier/list_models/")

        self.assertEqual(response.status_code, 200, "The API request should return a 200 status code for success")

        if response.content:
            response_data = json.loads(response.content)

            self.assertIn('success', response_data, "The response should contain a 'response_data' key")
            self.assertIn('result', response_data, "The response should contain a 'result' key")
            
            data = response_data['result']
            self.assertIn('models', data, "The response should contain a 'models' key in 'result'")
            
            models_name = data['models']
            self.assertIsInstance(models_name, list, "The response should contain a models name list")
            
    def test_predict(self):
        """
        Tests the 'predict_data' function for various scenarios:

        - Invalid JSON request (not valid JSON format).
        - Missing 'values' key in the request body.
        - Request body with 'values' key containing non-integer values.
        - Successful prediction with a list of integers in the 'values' key (no model name specified).
        - Successful prediction with a list of integers in the 'values' key and a recognized model name.
        - Successful prediction with a list of integers in the 'values' key and an unrecognized model name.
        """
        
        client = Client()
        
        ############
        # Invalid JSON request
        ############
        response = client.post('http://127.0.0.1:8000/api/number-classifier/predict/', data='not json"}', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Request body does not contain valid JSON.', response.json().get('error'))
        
        ###############
        # Missing 'values' key
        ############
        response = client.post(
            'http://127.0.0.1:8000/api/number-classifier/predict/', 
            json={}, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.content)
        
        self.assertIn('success', response_data, "The response should contain a 'success' key")
        success = response_data['success']
        self.assertEqual(success, False, "The value of the 'success' key should be False")
        
        self.assertIn('result', response_data, "The response should contain a 'result' key")
        result = response_data['result']
        self.assertIsInstance(result, dict, "The value of the 'result' key should be dictionary")

        self.assertIn('error_msg', result, "The response should contain a 'error_msg' key")
        error_msg = result['error_msg']
        self.assertIn("The 'values' key missing", error_msg)
        
        ############
        # Non-integer values
        ############
        invalid_data = {'values': ['a', 'b', 'c']}
        response = client.post(
            'http://127.0.0.1:8000/api/number-classifier/predict/', 
            json=invalid_data, 
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(False, response.json().get('success', ''), "The value of the 'success' key should be False")
        self.assertIn("The 'values' elements must be integers", response.json().get('result', {}).get('error_msg'))
        
        ############
        # Test successful prediction
        ############
        valid_data = {
            'values': [0, 1, 2, 3, 4, 5]
        }
        result_data = {
                'success': True,
                'result': {
                    'classification': [
                        [0, "FizzBuzz"], 
                        [1, "None"], 
                        [2, "None"], 
                        [3, "Fizz"], 
                        [4, "None"], 
                        [5, "Buzz"],
                    ]
                }
            }
        
        response = client.post(
            'http://127.0.0.1:8000/api/number-classifier/predict/', 
            json=valid_data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result_data, 'Classification fails without specifying the model')

        ############
        # Valid request with model name (recognized)
        ############
        valid_data['model_name'] = 'decision_tree'
        response = client.post(
            'http://127.0.0.1:8000/api/number-classifier/predict/', 
            json=valid_data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result_data, 'Classification fails with specifying the model')

        ############
        # Valid request with model name (unrecognized)
        ############
        valid_data['model_name'] = 'unknown_model'
        response = client.post(
            'http://127.0.0.1:8000/api/number-classifier/predict/', 
            json=valid_data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Model name is not recognized", response.json().get('result', {}).get('error_msg'))
        
        
    
    