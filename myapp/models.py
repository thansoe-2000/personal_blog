from django.db import models

# Create your models here.

class Experience(models.Model):
    time = models.CharField(max_length=20)
    carrier = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.carrier

 


