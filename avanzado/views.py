from avanzado.models import Vehiculo
from avanzado.forms import BusquedaVehiculo

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


       

class ListaVehiculos(ListView):
    model = Vehiculo
    # success_url = '/avanzado/vehiculos/'
    template_name = 'avanzado/ver_vehiculos.html'
    fields = ['matricula', 'propietario', 'modelo', 'marca', 'cant_puertas', 'color', 'avatar'] ######
    
    def get_queryset(self):
        matricula = self.request.GET.get('matricula', '')
        if matricula:
            object_list = self.model.objects.filter(matricula__icontains=matricula)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaVehiculo()
        return context    
    
class CrearVehiculo(LoginRequiredMixin, CreateView):
    model  = Vehiculo
    success_url = '/avanzado/vehiculos/'
    template_name = 'avanzado/crear_vehiculo.html'
    fields = ['matricula', 'propietario', 'modelo', 'marca', 'cant_puertas', 'color', 'chasis']
     
        
class EditarVehiculo(LoginRequiredMixin, UpdateView):
    model  = Vehiculo
    success_url = '/avanzado/vehiculos/'
    template_name = 'avanzado/editar_vehiculo.html'
    fields = ['matricula', 'propietario', 'modelo', 'marca', 'cant_puertas', 'color']    #
   
    
class EliminarVehiculo(LoginRequiredMixin, DeleteView):
    model  = Vehiculo
    success_url = '/avanzado/vehiculos/'###esta en mayusculas Vehiculos
    template_name = 'avanzado/eliminar_vehiculo.html'    
    
