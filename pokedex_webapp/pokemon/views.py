from django.shortcuts import render
from .services import get_pokemon

def home(request):
     print(get_pokemon())
     context = {
          'pokemon': get_pokemon()
     }
     return render(request, './pages/home.html', context)

def pokemon(request, order):
     print(get_pokemon(order=order))
     context = {
          'pokemon': get_pokemon(order=order)
     }
     return render(request, './pages/pokemon.html', context)