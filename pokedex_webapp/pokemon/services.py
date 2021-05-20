import json
import requests
from django.conf import settings

def get_pokemon(order=None):
    # get_pokemon to get all pokemon
    # get_pokemon(order) to get specific pokemon

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
    # get all pokemon types

    response = requests.get(settings.API_URL + 'type/')
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def new_pokemon(request):
    # create new pokemon

    response = requests.post(settings.API_URL + 'pokemon/', request )
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def edit_pokemon(request, order):
    # edit pokemon

    response = requests.put(settings.API_URL + 'pokemon/' + str(order) + '/', request )
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def delete_pokemon(request, order):
    # delete pokemon

    response = requests.delete(settings.API_URL + 'pokemon/' + str(order) + '/')
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None

def create_sprite(request, order=None):
    # create/update pokemon sprite
    response = requests.post(settings.API_URL  +'pokemon/' + str(order) + '/' + 'upload-sprite/', files=request)
        
    if response.status_code == 200:
        json_response = response.json()
        return json_response
    else:
        return None