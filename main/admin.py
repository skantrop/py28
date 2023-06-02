from django.contrib import admin

from main.models import Musician, Grammy, Song

admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Grammy)
