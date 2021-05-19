from urllib.request import urlopen
from django.core.files import File
from django.db import models
from django.core.files.temp import NamedTemporaryFile


def sprite_file(self, filename):
    return '/'.join( ['sprite', str(self.id)], filename)

class Pokemon(models.Model):
    name = models.CharField(max_length=100, blank=False)
    sprite = models.ImageField(upload_to='sprite_file', blank=True)
    main_type = models.ForeignKey('pokemon.Type', on_delete=models.PROTECT, related_name='main_type', default=None)
    sub_type = models.ForeignKey('pokemon.Type', on_delete=models.PROTECT, related_name='sub_type', default=None, null=True)

    def get_prev(self):
        print('heh')
        id = self.id - 1
        p_item = ''
        while p_item == '' and id>=0:
            try:
                print(id)
                p_item = Pokemon.objects.get(id=id).id
            except:
                id-=1
        return p_item

    def get_next(self):
        id = self.id + 1
        n_item = ''
        while n_item == '' and id<=Pokemon.objects.all().last().id:
            try:
                n_item = Pokemon.objects.get(id=id).id
            except:
                id+=1
        return n_item

    def get_sprite(self, url):
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        self.sprite.save(self.name + ".png", File(img_temp))

class Type(models.Model):
    name = models.CharField(max_length=100, blank=False)
    # color = models.CharField(max_length=6, blank=False)

    def get_pokemons(self):
        pokemons = Pokemon.objects.filter(main_type=self) | Pokemon.objects.filter(sub_type=self)
        return pokemons