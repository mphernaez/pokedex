import json
import requests
from django.conf import settings

def get_pokemon(order=None):
    if order:
        response = requests.get(settings.API_URL + 'pokemon/' + str(order))
    else:
        response = requests.get(settings.API_URL + 'pokemon/')
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def get_type():
    response = requests.get(settings.API_URL + 'type/')
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def edit_pokemon(request, order):
    response = requests.put(settings.API_URL + 'pokemon/' + str(order) + '/', request )
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None