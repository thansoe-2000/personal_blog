from django.contrib import admin
from . models import *
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'time', 'carrier', 'company', 'location', 'description']

class EducationAdmin(admin.ModelAdmin):
    list_display =['id', 'time', 'collage', 'location', 'major', 'description']
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)


