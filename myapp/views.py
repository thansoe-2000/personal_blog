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




