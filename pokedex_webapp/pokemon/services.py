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