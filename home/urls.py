from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    path('busqueda-personas/', views.busqueda_personas, name ='busqueda_personas'),    
    path('about/', views.about, name='about'),
]

