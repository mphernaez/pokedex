import json
from django.shortcuts import render

from .models import Pokemon, Type
from .serializers import PokemonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import viewsets
from rest_framework import permissions
from pokemon.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.AllowAny]

