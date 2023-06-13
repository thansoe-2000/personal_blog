from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=20)
    background = models.ImageField(upload_to='hero-image')
    carrier = models.CharField(max_length=50)

    def __str__(self):
        return self.name