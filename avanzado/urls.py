from django.urls import path
from avanzado import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/crear/', views.crear_mascotas, name='crear_mascotas')
]
