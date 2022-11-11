from django.urls import path
from avanzado import views
from django.conf import settings
from django.conf.urls.static import static #
 
urlpatterns = [
    #version con vistas comunes
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name='eliminar_mascota'),
    
    #version con clases basadas en vistas
    path('vehiculos/', views.ListaVehiculos.as_view(), name='ver_vehiculos'),
    path('vehiculos/crear/', views.CrearVehiculo.as_view(), name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>', views.EditarVehiculo.as_view(), name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>', views.EliminarVehiculo.as_view(), name='eliminar_vehiculo'),
    # path('vehiculos/busqueda/<int:pk>', views.BusquedaVehiculo.as_view(), name='busqueda_vehiculo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#