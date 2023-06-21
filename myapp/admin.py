from django.contrib import admin
from . models import *
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'body', 'image'
    ]
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name']





class SkillAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'body']





admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Skill, SkillAdmin)

