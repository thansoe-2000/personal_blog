from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('project/', views.project, name='projectpage'),
    path('contact/', views.contact, name='contactpage'),
    


   
]