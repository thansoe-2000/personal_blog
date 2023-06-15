from django.urls import path
from . import views

urlpatterns = [
    path('main-page', views.main, name='main_page'),
    path('', views.hero, name='heropage'),
    path('about/', views.about, name='aboutpage'),
    # path('service/', views.service, name='servicepage'),
    path('skill/', views.skill, name='skillpage'),
    path('gallary/', views.gallary, name='gallarypage'),
    path('contact/', views.contact, name='contactpage'),


    # back admin-dashboard
    path('dashboard/', views.index, name='index_dashboard'),
]