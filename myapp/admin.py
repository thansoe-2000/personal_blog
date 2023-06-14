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
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name']


class GallaryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'category', 'title', 'image']

admin.site.register(Hero, HeroAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallary, GallaryAdmin)
