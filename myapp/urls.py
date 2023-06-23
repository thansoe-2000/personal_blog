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

    path('dashboard/education', views.education, name='education_page'),
    path('dashboard/education/edit<str:pk>/', views.edit_edu, name='edit_edu'),
    


   
]