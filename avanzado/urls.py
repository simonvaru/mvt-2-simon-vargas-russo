from django.urls import path
from avanzado import views
from django.conf import settings
from django.conf.urls.static import static #
 
urlpatterns = [  
    path('vehiculos/', views.ListaVehiculos.as_view(), name='ver_vehiculos'),
    path('vehiculos/crear/', views.CrearVehiculo.as_view(), name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>', views.EditarVehiculo.as_view(), name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>', views.EliminarVehiculo.as_view(), name='eliminar_vehiculo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#