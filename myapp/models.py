from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Experience(models.Model):
    time = models.CharField(max_length=20)
    carrier = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.carrier

class Education(models.Model):
    time = models.CharField(max_length=100)
    collage = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):
        return self.major
 

class Pro_skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()
    image = models.ImageField(upload_to='project-image')
   

    def __str__(self):
        return self.name 
    
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname