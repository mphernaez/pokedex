import requests
from django.conf import settings

from django.core.management.base import BaseCommand, CommandError
from pokemon.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Initalize Pokemons [0-893]'

    def add_arguments(self, parser):
        parser.add_argument('limit', nargs='+', type=int)

    def handle(self, *args, **options):
        url = settings.POKEMON_API_ENDPOINT + 'type'
        r = requests.get(url = url)
        types = r.json()
        number = 1
        
        for t in types['results']:
            Type.objects.create(
                name=t['name'],
            )
            number+=1
        limit = options['limit'][0]
        number = 1

        while number <= limit:
            url = settings.POKEMON_API_ENDPOINT + 'pokemon/' + str(number)
            r = requests.get(url = url)
            pokemon = r.json()
            p = Pokemon.objects.create(
                name=pokemon['name'],
                sprite=pokemon['sprites']['front_default'],
                main_type=Type.objects.get(name=pokemon['types'][0]['type']['name']),
            )
            try:
                p.sub_type=Type.objects.get(
                    name=pokemon['types'][1]['type']['name'],
                    )
                p.save()
            except:
                print('no sub_type')
            print(p)
            number+=1
        