from django.http import HttpResponse
from datetime import datetime

def hola(request):
    return HttpResponse("Buenas, clase 41765!")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento aproxinmada para tus {edad} años seria: {fecha}")