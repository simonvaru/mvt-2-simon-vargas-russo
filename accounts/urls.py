from re import template
from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.mi_login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'), 
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
    path('about/', views.about, name='about'),
    path('consignas/', views.consignas, name='consignas'),
]

