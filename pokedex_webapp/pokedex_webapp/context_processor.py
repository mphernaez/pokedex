# project/context_processors.py
from django.conf import settings

def urls(request):
    return {
        'MEDIA_URL': settings.API_URL + 'media',
        'BASE_URL': settings.BASE_DIR
        }  