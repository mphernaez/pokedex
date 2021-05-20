import requests
from django.conf import settings
from django.core import files
from io import BytesIO
from django.shortcuts import get_object_or_404

from django.core.management.base import BaseCommand, CommandError
from pokemon.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Initalize Pokemons [0-893]'

    def add_arguments(self, parser):
        parser.add_argument('limit', nargs='+', type=int)

    def handle(self, *args, **options):

        #initalize types
        try:
            ts = Type.objects.get(id=1)
            print('types already exist')
        except:
            url = settings.POKEMON_API_ENDPOINT + 'type'
            r = requests.get(url = url)
            types = r.json()
            number = 1
            
            for t in types['results']:
                Type.objects.create(
                    name=t['name'],
                ).save()
                number+=1

        #initalize pokemon from 1 to {{limit}}
        limit = options['limit'][0]
        number = 1

        while number <= limit:
            url = settings.POKEMON_API_ENDPOINT + 'pokemon/' + str(number)
            r = requests.get(url = url)
            
            pokemon = r.json()
            p = Pokemon.objects.create(
                name=pokemon['name'],
                main_type=Type.objects.get(name=pokemon['types'][0]['type']['name']),
            )

            url = pokemon['sprites']['front_default']
            p.get_sprite(url)
            p.save()

            print(p.name)
            try:
                p.sub_type=Type.objects.get(
                    name=pokemon['types'][1]['type']['name'],
                    )
                p.save()
            except:
                print('no sub_type')
            
            number+=1
        