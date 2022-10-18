from django.urls import path
from avanzado import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>', views.editar_mascotas, name='editar_mascota'),
]
