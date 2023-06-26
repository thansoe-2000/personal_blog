from django.urls import path
from . import views

urlpatterns = [
    # frontend
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('project/', views.project, name='projectpage'),
    path('contact/', views.contact, name='contactpage'),
    

    # backend
    path('dashboard/', views.index, name='indexpage'),
    path('dashboard/experience', views.experience, name='experience_page'),
    path('dashboard/experience/edit<str:pk>/', views.experience_edit, name='experience_edit'),

    # education 
    path('dashboard/education', views.education, name='education_page'),
    path('dashboard/education/edit<str:pk>/', views.edit_edu, name='edit_edu'),

    # language
    path('dashboard/language', views.language, name='language_page'),
    path('dashboard/language/edit<str:pk>/', views.edit_language, name='edit_language'),

    # pro skill
    path('dashboard/proskill', views.proskill, name='proskill_page'),

    # projects
    path('dashboard/project/', views.backend_project, name='project_page'),
    


   
]