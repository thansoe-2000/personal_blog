from django.shortcuts import render, redirect
from . models import *
from . forms import *
def main(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'projects/home.html')

def about(request):
    abouts = About.objects.first()
    context = {
        'abouts':abouts
    }
    return render(request, 'projects/about.html', context)

def project(request):
    return render(request, 'projects/projects.html')


def contact(request):
    return render(request, 'projects/contact.html')




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

def skilladmin(request):
    page = 'skill_create'
    form = SkillForm()
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('skill_admin')
    context = {
        'page':page,
        'form':form,
        'skills':skills
    }
    return render(request, 'back/skill.html', context)
