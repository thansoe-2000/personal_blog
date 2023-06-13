from django.shortcuts import render, redirect

def main(request):
    return render(request, 'pages/main.html')

def hero(request):
    return render(request, 'pages/hero.html')

def about(request):
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/services.html')

def skill(request):
    return render(request, 'pages/skill.html')

def contact(request):
    return render(request, 'pages/contact.html')


# backend dashboard
def index(request):
    return render(request, 'back/index.html')