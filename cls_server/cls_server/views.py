from django.shortcuts import render

import json
from django.http import JsonResponse
from django.http import HttpResponse

from logic.classifier import MyClassifier
from logic.dataset.numbers import load, number2remainder

classifier = MyClassifier()
classifier.build_models(load((1000, 2000, 1), (1, 100, 1)))


def process_data(request):
    """
    Petición web que recibe un JSON y devuelve otro JSON como respuesta.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        JsonResponse: Respuesta JSON con un diccionario como contenido.
    """

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Request body does not contain valid JSON.'}, status=400)

    try:
        _valid_structure(data) 
    except Exception as error:
        return JsonResponse({
            'success': False, 
            'result': {
                'error_msg': str(error)
            }
        })

    return JsonResponse({
        'success': True, 
        'result': _process_logic(data)}
    )

def _valid_structure(json: dict) -> None:
    """
    Validates the structure of a JSON dictionary according to specific requirements.

    Args:
        json (dict): 
            The JSON dictionary to be validated.

    Raises:
        AssertionError: If the structure of the dictionary is invalid.
    
    """
    assert 'values' in json, "The 'values' key missing."

    values = json["values"]
    assert isinstance(values, list), "The 'values' value must be a list."

    for elemento in values:
        assert isinstance(elemento, int), "The 'values' elements must be integers."

    if 'model_name' in json:
        print(classifier.model_names())
        assert json['model_name'] in classifier.model_names() , "Model name is not recognized"
    
def _process_logic(data: dict):
    """Processes input data and returns classifications

    Args:
        data (dict): 
            Data to process. It is expected that you will have the following keys:
                values (list[int]): List of values to classify.
                model_name (str): Name of the model to use for classification. It is not required.

    Returns:
        dict: 
            Dictionary with the key 'classification' which contains a list of tuples (int, str). Each number corresponds to the one defined and the string is the classification obtained.

    """
    model_name = data.get('model_name')
    return {
        'classification': [
            (
                value, 
                classifier.predict(
                    value, 
                    lambda x: [number2remainder(x)], 
                    model_name
                )
            ) for value in data['values']
        ]
    }

def list_classifiers():
    pass