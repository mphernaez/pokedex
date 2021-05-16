from .models import Pokemon, Type
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class PokemonSerializer(serializers.ModelSerializer):
    main_type = TypeSerializer(many=False, read_only=True)
    sub_type = TypeSerializer(many=False, read_only=True)
    prev = serializers.SerializerMethodField()
    next = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'sprite', 'main_type', 'sub_type', 'prev', 'next']

    def get_prev(self, obj):
        return Pokemon.objects.get(id=obj.id).get_prev()

    def get_next(self, obj):
        return Pokemon.objects.get(id=obj.id).get_next()