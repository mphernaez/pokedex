import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, Type
from .serializers import PokemonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import viewsets
from rest_framework import permissions
from pokemon.serializers import PokemonSerializer, TypeSerializer


class PokemonView(viewsets.ModelViewSet):
    """
    API endpoint that allows pokemon to be viewed or edited.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, request, pk):

        pokemon = Pokemon.objects.get(id=pk)
        pokemon.name = request.POST.get('name', pokemon.name)
        pokemon.main_type = Type.objects.get(id=request.POST.get('main_type', pokemon.main_type.id))

        if request.POST.get('sub_type') != '':
            pokemon.sub_type = Type.objects.get(id=request.POST.get('sub_type', pokemon.sub_type.id))
        else:
            pokemon.sub_type = ''
            
        print(pokemon.sub_type.name)
        return JsonResponse({'status':'200'})



class TypeView(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.AllowAny]

