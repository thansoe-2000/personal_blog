from django.shortcuts import render, redirect
from . models import *

def main(request):
    return render(request, 'pages/main.html')

def hero(request):
    heros = Hero.objects.all()
    abouts = About.objects.all()
    context = {
        'heros':heros,
        'abouts':abouts
    }
    return render(request, 'pages/hero.html', context)

def about(request):
    abouts = About.objects.all()
    context = {
        'abouts':abouts
    }
    return render(request, 'pages/about.html', context)

def service(request):
    return render(request, 'pages/services.html')

def skill(request):
    return render(request, 'pages/skill.html')

def contact(request):
    return render(request, 'pages/contact.html')


# backend dashboard
def index(request):
    return render(request, 'back/index.html')