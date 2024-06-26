from django.shortcuts import render

import json
from django.http import JsonResponse

def procesar_json(request):
    """
    Petición web que recibe un JSON y devuelve otro JSON como respuesta.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        JsonResponse: Respuesta JSON con un diccionario como contenido.
    """

    print('aqui estoy')
    # Obtenga el JSON del cuerpo de la solicitud
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'El cuerpo de la solicitud no contiene un JSON válido.'}, status=400)

    # Valide la estructura del JSON recibido (opcional)
    # ...

    # Procese el JSON recibido y genere la respuesta
    respuesta = procesar_logica_json(data)  # Implemente la lógica de procesamiento aquí

    # Convierta la respuesta a un diccionario de Python
    respuesta_dict = {'datos': respuesta}

    # Devuelva la respuesta como un JSON
    return JsonResponse(respuesta_dict)




def procesar_logica_json(data):
    # Suponiendo que el JSON recibido tiene una clave "operacion" y un valor "suma"
    if data['operacion'] == 'suma':
        resultado = data['valor1'] + data['valor2']
    elif data['operacion'] == 'resta':
        resultado = data['valor1'] - data['valor2']
    else:
        resultado = "Operación no válida."

    return resultado