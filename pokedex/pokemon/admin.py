from django.contrib import admin

from .models import Pokemon, Type
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

class FirstLetterListFilter(admin.SimpleListFilter):
    title = _('First letter')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'letter'

    def lookups(self, request, model_admin):
        return (
            ('A', _('A')),
            ('B', _('B')),
            ('C', _('C')),
            ('D', _('D')),
            ('E', _('E')),
            ('F', _('F')),
            ('G', _('G')),
            ('H', _('H')),
            ('I', _('I')),
            ('J', _('J')),
            ('K', _('K')),
            ('L', _('L')),
            ('M', _('M')),
            ('N', _('N')),
            ('O', _('O')),
            ('P', _('P')),
            ('Q', _('Q')),
            ('R', _('R')),
            ('X', _('X')),
            ('T', _('T')),
            ('U', _('U')),
            ('V', _('V')),
            ('W', _('W')),
            ('X', _('X')),
            ('Y', _('Y')),
            ('Z', _('Z')),
        
        )

    def queryset(self, request, queryset):
        try:
            q = queryset.filter(name__startswith=self.value())
        except:
            q = queryset.all()
        return q


class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = (FirstLetterListFilter, 'main_type', 'sub_type')

    def get_ordering(self, request):
        return [('id')]


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

    def get_ordering(self, request):
        return [('id')]

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)
