from django.shortcuts import redirect, render
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario

def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'avanzado/ver_mascotas.html', {'mascotas': mascotas})

def crear_mascotas(request):
    
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
    
    formulario = MascotaFormulario()
    
    return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})