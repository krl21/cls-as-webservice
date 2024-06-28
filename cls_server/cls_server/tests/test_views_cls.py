
from django.test import TestCase
import requests
import json

class NumberClassifierTestCase(TestCase):
    
    def test_list_cls(self):
        
        assert True == False, 'Error absurdo'
        
        # Define the data to be sent in the POST request (if needed)
        data = {}  # Replace with actual data if the API endpoint expects it

        # Send a GET request to the API endpoint
        response = requests.get("http://127.0.0.1:8000/api_classifier/list_models/", json=data)

        # Check the status code of the response
        self.assertEqual(response.status_code, 200, "The API request should return a 200 status code for success")

        # Validate the response content (optional)
        # Assuming the response is JSON, you can parse it and check specific fields:
        if response.content:
            response_data = json.loads(response.content)
            # Add assertions to validate the response data (e.g., number of models, model names)
            self.assertIn('models', response_data, "The response should contain a 'models' key")
            # ... (add more assertions as needed)
        

        
        
    
    