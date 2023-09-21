from django.contrib import admin

from .models import Artist, Genra, Album, Song

admin.site.register([Artist, Genra, Album, Song])