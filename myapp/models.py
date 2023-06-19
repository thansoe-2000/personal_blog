from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=20)
    background = models.ImageField(upload_to='hero-image')
    carrier = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    
    class  Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='aboutimage')
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        ordering = ['-created_at']
        
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

class Skill(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name =  models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=20)

    def __str__(self):
        return self.address