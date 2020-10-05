from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User    #, A1, A2, A3, A4, A5, A6, Counter


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login','date_of_birth','gender','country')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'name', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login','date_of_birth','gender','country')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)

                                    # --- Levels A1 A2 A3 A4 A5 A6 --- #

'''class A1Full(admin.ModelAdmin):
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

                                 # --- Counters --- #

class CounterFull(admin.ModelAdmin):
    list_display = ("id", "language", "languagetwo", "email", "a1", "a2", "a3", "a4", "a5", "a6")
    search_fields = ("id", "language", "languagetwo", "email", "a1", "a2", "a3", "a4", "a5", "a6")

admin.site.register(Counter, CounterFull)'''