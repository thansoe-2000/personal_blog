from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=20)
    background = models.ImageField(upload_to='hero-image')
    carrier = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='aboutimage')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Gallary(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallary-image', null=True, blank=True)

    def __str__(self):
        return self.title
