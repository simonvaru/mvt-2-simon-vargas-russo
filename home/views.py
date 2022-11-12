# from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
import random
from home.forms import HumanoFormulario, BusquedaHumanoFormulario

from home.models import Humano




def crear_persona(request):
    
    if request.method == "POST":
        
        formulario = HumanoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            # fecha_creacion = data.get('fecha_creacion', datetime.now())
            fecha_creacion = data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion = datetime.now()
            
            persona = Humano(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()
        
            return redirect('ver_personas')
        
    formulario = HumanoFormulario()
    
    return render(request, 'home/crear_persona.html', {'formulario': formulario})

def ver_personas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Humano.objects.filter(nombre__icontains=nombre)
    else:    
        personas = Humano.objects.all()

    formulario = BusquedaHumanoFormulario()

    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario} )
    
def index(request):
        
    return render(request, 'home/index.html')







