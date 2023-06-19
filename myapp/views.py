from django.shortcuts import render, redirect
from . models import *
from . forms import *
def main(request):
    return render(request, 'pages/main.html')

def hero(request):
    heros = Hero.objects.first()
    abouts = About.objects.first()
    skills = Skill.objects.all()
    context = {
        'heros':heros,
        'abouts':abouts,
        'skills':skills
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
    skills = Skill.objects.all()
    context = {
        'skills':skills
    }
    return render(request, 'pages/skill.html', context)

def gallary(request):
    categorys = Category.objects.all()
    gallarys = Gallary.objects.all()
    context = {
        'gallarys':gallarys,
        'categorys':categorys
    }
    return render(request, 'pages/gallary.html', context)
def contact(request):
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'pages/contact.html', context)

def contactinfo(request):
    contactinfos = ContactInfo.objects.all()
    context = {
        'contactinfos':contactinfos
    }
    return render(request, 'pages/contact.html', context)

# backend dashboard
def index(request):
    return render(request, 'back/index.html')

def category(request):
    return render(request, 'back/category.html')

def adminhero(request):
    page = 'hero_create'
    form = HeroForm()
    heros = Hero.objects.all()
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('hero_admin')
    context = {
        'form':form,
        'heros':heros,
        'page':page
    }
    return render(request, 'back/hero.html', context)

def adminabout(request):
    page = 'about_create'
    form = AboutForm()
    abouts = About.objects.all()
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('about_admin')

    context = {
        'page':page,
        'form':form,
        'abouts':abouts
    }
    return render(request, 'back/about.html', context)