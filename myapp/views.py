from django.shortcuts import render, redirect
from . models import *
from . forms import *

# frontend
def home(request):
    return render(request, 'projects/home.html')

def about(request):
    educations = Education.objects.all()[0:3]
    experiences = Experience.objects.all()[0:3]
    languages = Language.objects.all()[0:5]
    proskills = Pro_skill.objects.all()[0:5]

    context = {
        'experiences':experiences,
        'educations':educations,
        'languages':languages,
        'proskills':proskills
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

def experience_edit(request, pk):
    page = 'edit_experience'
    experiences = Experience.objects.all()
    experience = Experience.objects.get(id=pk)
    form = ExperienceForm(instance=experience)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
        return redirect('experience_page')
    context = {
        'page':page,
        'experiences':experiences,
        'experience':experience,
        'form':form
    }
    return render(request, 'backend/experience.html', context)


def education(request):
    page = 'create_education'
    educations = Education.objects.all()
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('education_page')
    context = {
        'page':page,
        'educations':educations,
        'form':form
    }
    return render(request, 'backend/education.html', context )

def edit_edu(request, pk):
    page = 'edit_edu'
    educations = Education.objects.all()
    education = Education.objects.get(id=pk)
    form = EducationForm(instance=education)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
        return redirect('education_page')
    context = {
        'page':page,
        'educations':educations,
        'education':education,
        'form':form
    }
    return render(request, 'backend/education.html', context)


def language(request):
    page = 'create_language'
    form = LanguageForm()
    languages = Language.objects.all()
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('language_page')
    context = {
        'page':page,
        'form':form,
        'languages':languages,
        
    }
    return render(request, 'backend/language.html', context)

def edit_language(request, pk):
    page = 'edit_language'
    language = Language.objects.get(id=pk)
    form = LanguageForm(instance=language)
    languages = Language.objects.all()
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
        return redirect('language_page')
    context = {
        'page':page,
        'form':form,
        'language':language,
        'languages':languages
    }
    return render(request, 'backend/language.html', context)


def proskill(request):
    page = 'proskill_create'
    form = Pro_skillForm()
    proskills = Pro_skill.objects.all()
    if request.method == 'POST':
        form = Pro_skillForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('proskill_page')
    context = {
        'page':page,
        'form':form,
        'proskills':proskills
    }
    return render(request, 'backend/pro_skill.html', context)