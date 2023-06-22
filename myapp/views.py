from django.shortcuts import render, redirect
from . models import *
from . forms import *

# frontend
def home(request):
    return render(request, 'projects/home.html')

def about(request):
    experiences = Experience.objects.all()[0:3]
    context = {
        'experiences':experiences
    }
    return render(request, 'projects/about.html', context)

def project(request):
    return render(request, 'projects/projects.html')
    
def contact(request):
    return render(request, 'projects/contact.html')


# backend
def index(request):
    return render(request, 'backend/index.html')


def experience(request):
    page = 'create_experience'
    experiences = Experience.objects.all()
    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('experience_page')
    context = {
        'experiences':experiences,
        'form':form,
        'page':page
    }
    return render(request, 'backend/experience.html', context)






