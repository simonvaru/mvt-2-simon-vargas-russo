from re import template
from django.shortcuts import redirect, render
from avanzado.models import Mascota, Vehiculo
from avanzado.forms import MascotaFormulario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'avanzado/ver_mascotas.html', {'mascotas': mascotas})


@login_required
def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST) 
     

        if formulario.is_valid():
            datos=formulario.cleaned_data
           
            mascota = Mascota(
               nombre=datos['nombre'], 
               tipo=datos['tipo'], 
               edad=datos['edad'], 
               fecha_nacimiento=datos['fecha_nacimiento']
            )
            mascota.save()
            return redirect('ver_mascotas')
    
        else:
            return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario})
    
    formulario = MascotaFormulario()
    
    return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})

@login_required
def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST) 
     

        if formulario.is_valid():
            datos=formulario.cleaned_data
                        
            mascota.nombre = datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            mascota.save()
            return redirect('ver_mascotas')
        
    formulario = MascotaFormulario(
        initial={
            'nombre': mascota.nombre, 
            'tipo': mascota.tipo,
            'edad': mascota.edad, 
            'fecha_nacimiento': mascota.fecha_nacimiento
        }
    )
    
    return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario, 'mascota':mascota})  

@login_required
def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')   
        
class ListaVehiculos(ListView):
    model = Vehiculo
    template_name = 'avanzado/ver_vehiculos.html'
    
    
class CrearVehiculo(LoginRequiredMixin, CreateView):
    model  = Vehiculo
    success_url = '/avanzado/vehiculos/'
    template_name = 'avanzado/crear_vehiculo.html'
    fields = ['modelo', 'marca', 'cant_puertas', 'color', 'chasis']
     
        
class EditarVehiculo(LoginRequiredMixin, UpdateView):
    model  = Vehiculo
    success_url = '/avanzado/vehiculos/'
    template_name = 'avanzado/editar_vehiculo.html'
    fields = ['modelo', 'marca', 'cant_puertas', 'color']    
   
    
class EliminarVehiculo(LoginRequiredMixin, DeleteView):
    model  = Vehiculo
    success_url = '/avanzado/Vehiculos/'
    template_name = 'avanzado/eliminar_vehiculo.html'    
      
# class VerMascota():    
