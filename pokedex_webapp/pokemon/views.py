from django.shortcuts import render
from .services import get_pokemon

def home(request):
     print(get_pokemon())
     context = {
          'pokemon': get_pokemon()
     }
     return render(request, './pages/home.html', context)