from django.contrib import admin
from . models import *
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'background', 'carrier'
    ]

class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'body', 'image'
    ]

admin.site.register(Hero, HeroAdmin)
admin.site.register(About, AboutAdmin)
