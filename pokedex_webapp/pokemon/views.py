import json
from django.http import HttpResponse
from django.shortcuts import render
from .services import get_pokemon, get_type, edit_pokemon, delete_pokemon, create_sprite, new_pokemon

def home(request):
     context = {
          'pokemon': get_pokemon(),
          'types': get_type(),
     }
     return render(request, './pages/home.html', context)

def pokemon(request, order):
     context = {
          'pokemon': get_pokemon(order=order),
          'types': get_type(),
     }

     if request.method == 'POST':
          if order:
               edit_pokemon(request.POST, order)
               return HttpResponse(status=200)
          
     if request.method == 'DELETE':
          delete_pokemon(request.POST, order)
          return HttpResponse(status=200)

     return render(request, './pages/pokemon.html', context)

def create_pokemon(request):
     print(request.POST)
     r = new_pokemon(request.POST)
     return HttpResponse(json.dumps(r), status=200)
     

def upload_sprite(request, order):
     context = {
          'pokemon': get_pokemon(order=order),
          'types': get_type(),
     }
     if request.method == 'POST':
          create_sprite(request.FILES, order)
          return HttpResponse(status=200)
     # return render(request, './pages/pokemon.html', context)

