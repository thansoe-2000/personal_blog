from django.shortcuts import render, redirect
from . models import *

def main(request):
    return render(request, 'pages/main.html')

def hero(request):
    heros = Hero.objects.first()
    abouts = About.objects.first()
    context = {
        'heros':heros,
        'abouts':abouts
    }
    return render(request, 'pages/hero.html', context)

def about(request):
    abouts = About.objects.first()
    context = {
        'abouts':abouts
    }
    return render(request, 'pages/about.html', context)

# def service(request):
#     return render(request, 'pages/services.html')

def skill(request):
    return render(request, 'pages/skill.html')

def gallary(request):
    categorys = Category.objects.all()
    gallarys = Gallary.objects.all()
    context = {
        'gallarys':gallarys,
        'categorys':categorys
    }
    return render(request, 'pages/gallary.html', context)
def contact(request):
    return render(request, 'pages/contact.html')


# backend dashboard
def index(request):
    return render(request, 'back/index.html')