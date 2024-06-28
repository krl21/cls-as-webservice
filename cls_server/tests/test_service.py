
from django.test import TestCase
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
            
        

        
        
    
    