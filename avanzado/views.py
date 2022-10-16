from django.shortcuts import render
from avanzado.models import Mascota


# Create your views here.
def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'ver_mascotas.html', {'mascotas': mascotas})