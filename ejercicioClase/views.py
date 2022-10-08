from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader

def hola(request):
    return HttpResponse("Buenas, clase 41765!")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento aproxinmada para tus {edad} años seria: {fecha}")

def mi_template(request):
    cargar_archivo = open(r'E:\python_proyects\curso\ejercicios_de_clase_18_c\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    # cargar_archivo = open(r'E:\python_proyects\curso\ejercicios_de_clase_18_c\templates\tu_template.html', 'r')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({'persona':nombre})
    # template_renderizado = template.render(contexto)
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)


    
