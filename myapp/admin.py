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


class SkillAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'body']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'phone', 'email', 'website']


admin.site.register(Hero, HeroAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallary, GallaryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
