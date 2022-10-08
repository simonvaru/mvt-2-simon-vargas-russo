from django.http import HttpResponse
from datetime import datetime

def hola(request):
    return HttpResponse("Buenas, clase 41765!")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")
