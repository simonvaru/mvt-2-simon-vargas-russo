from ssl import HAS_TLSv1_1
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
# from django.contrib.auth import login as django_login
from accounts.forms import EditarPerfilFormulario, MiFormularioDeCreacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user()
            login(request, usuario) #django_login(request, usuario)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        
    else:
        formulario = MiFormularioDeCreacion()    
    
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    ...
    return render(request, 'accounts/perfil.html', {})

@login_required
def editar_perfil(request):
    
    user = request.user
        
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.first_name = data_nueva['first_name']
            user.last_name = data_nueva['last_name']
            user.email = data_nueva['email']
            
            user.save()
            return redirect('perfil')
            
        
    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name, 
                'email': request.user.email,
            }
        )    
    
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})



class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_contrasenia.html'
    success_url = '/accounts/perfil/'



