from .models import Pokemon, Type
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class PokemonSerializer(serializers.ModelSerializer):
    main_type = TypeSerializer(many=False, read_only=True)
    sub_type = TypeSerializer(many=False, read_only=True)
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'sprite', 'main_type', 'sub_type']