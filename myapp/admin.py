from django.contrib import admin
from . models import *
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'time', 'carrier', 'company', 'location', 'description']

class EducationAdmin(admin.ModelAdmin):
    list_display =['id', 'time', 'collage', 'location', 'major', 'description']

class Pro_skillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class LanguageAdmin(admin.ModelAdmin):
    list_display =['id', 'name']

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Pro_skill, Pro_skillAdmin)
admin.site.register(Language, LanguageAdmin)


