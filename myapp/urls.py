from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('hero/', views.hero, name='heropage'),
    path('about/', views.about, name='aboutpage'),
    path('service/', views.service, name='servicepage'),
]