from django.urls import path
from . import views

urlpatterns = [
    path('main-page', views.main, name='main_page'),
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('project/', views.project, name='projectpage'),
    path('contact/', views.contact, name='contactpage'),
    


    # back admin-dashboard
    path('dashboard/', views.index, name='index_dashboard'),
    path('category/', views.category, name='category_page'),
    path('back/hero/', views.adminhero, name='hero_admin'),
    path('back/about/', views.adminabout, name='about_admin'),
    path('back/skill/', views.skilladmin, name='skill_admin'),
]