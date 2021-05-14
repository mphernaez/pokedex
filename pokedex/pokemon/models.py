from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, blank=False)
    sprite = models.CharField(max_length=100, blank=False, default='')
    main_type = models.ForeignKey('pokemon.Type', on_delete=models.PROTECT, related_name='main_type', default=None)
    sub_type = models.ForeignKey('pokemon.Type', on_delete=models.PROTECT, related_name='sub_type', default=None, null=True)


class Type(models.Model):
    name = models.CharField(max_length=100, blank=False)
    # color = models.CharField(max_length=6, blank=False)

    def get_pokemons(self):
        pokemons = Pokemon.objects.filter(main_type=self) | Pokemon.objects.filter(sub_type=self)
        return pokemons