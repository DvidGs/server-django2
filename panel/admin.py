from django.contrib import admin
from panel.models import A1, A2, A3, A4, A5, A6
# Register your models here.

class A1Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A1, A1Full)

class A2Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A2, A2Full)

class A3Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A3, A3Full)

class A4Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A4, A4Full)

class A5Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A5, A5Full)

class A6Full(admin.ModelAdmin):
    list_display = ("id", "category", "text")
    search_fields = ("id", "category", "text")

admin.site.register(A6, A6Full)