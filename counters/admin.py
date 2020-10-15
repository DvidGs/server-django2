from django.contrib import admin
from counters.models import Position

# Register your models here.

class PositionWords(admin.ModelAdmin):

    list_display = ('id', 'language_1', 'language_2', 'email', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')
    search_fields = ('id', 'language_1', 'language_2', 'email', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')

admin.site.register(Position, PositionWords)

