from django.contrib import admin
from . models import *
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'background', 'carrier'
    ]

admin.site.register(Hero, HeroAdmin)
