import json
from rest_framework.decorators import action
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

    def create(self, request):
        data = request.POST
        pokemon = Pokemon.objects.create(
            name=request.POST.get('name'),
            main_type=Type.objects.get(id=request.POST.get('main_type')),
        )
        if request.POST.get('sub_type') != '0':
            pokemon.sub_type = Type.objects.get(id=request.POST.get('sub_type'))
        else:
            pokemon.sub_type = None
        pokemon.save()
        return HttpResponse(json.dumps({'status': 200, 'id': pokemon.id}), status=200)

    def update(self, request, pk):

        pokemon = Pokemon.objects.get(id=pk)
        pokemon.name = request.POST.get('name', pokemon.name)
        pokemon.main_type = Type.objects.get(id=request.POST.get('main_type', pokemon.main_type.id))

        if request.POST.get('sub_type') != '0':
            pokemon.sub_type = Type.objects.get(id=request.POST.get('sub_type'))
        else:
            pokemon.sub_type = None

        pokemon.save()
        
        return HttpResponse(json.dumps({'status': 200}), status=200)

    @action(methods=['post'], url_path="upload-sprite", detail=True)
    def upload_sprite(self, request, pk):
        file = request.FILES['sprite']
        pokemon = Pokemon.objects.get(id=pk)
        pokemon.sprite.save(pokemon.name + ".png", file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)



class TypeView(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.AllowAny]

