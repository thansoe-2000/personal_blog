from django.urls import path
from . import views

urlpatterns = [
    path('main-page', views.main, name='main_page'),
    path('', views.hero, name='heropage'),
    path('about/', views.about, name='aboutpage'),
    # path('service/', views.service, name='servicepage'),
    path('skill/', views.skill, name='skillpage'),
    path('gallary/', views.gallary, name='gallarypage'),


    # back admin-dashboard
    path('dashboard/', views.index, name='index_dashboard'),
    path('category/', views.category, name='category_page'),
    path('back/hero/', views.adminhero, name='hero_admin'),
    path('back/about/', views.adminabout, name='about_admin'),
    path('back/skill/', views.skilladmin, name='skill_admin'),
]