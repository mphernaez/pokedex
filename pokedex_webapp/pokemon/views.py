from django.http import HttpResponse
from django.shortcuts import render
from .services import get_pokemon, get_type, edit_pokemon

def home(request):
     print(get_pokemon())
     context = {
          'pokemon': get_pokemon()
     }
     return render(request, './pages/home.html', context)

def pokemon(request, order):
     print(request.method)
     context = {
          'pokemon': get_pokemon(order=order),
          'types': get_type(),
     }

     if request.method == 'POST':
          edit_pokemon(request.POST, order)
          return HttpResponse(status=200)
     return render(request, './pages/pokemon.html', context)