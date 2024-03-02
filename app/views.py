from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evento
from .forms import  FormularioEventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm

# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def log(request):
    return render(request, 'registration/login.html')

def salir(request):
    logout(request)
    return redirect('inicio')

def register(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if  user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return  redirect ('eventos')
    return render(request, 'registration/register.html', data)
    
def nosotros(request):
    return render(request, 'pages/nosotros.html')

def base(request):
    return render(request, 'pages/base.html')

@login_required()
def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/index.html', {'eventos':  eventos})

def crear_evento(request):
    formulario = FormularioEventos(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('eventos')
    return render(request, 'eventos/crear.html', {'formulario': formulario})

def editar(request, id):
    evento = Evento.objects.get(id=id)
    formulario =  FormularioEventos (request.POST or None, request.FILES or None, instance=evento)
    if  formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('eventos')
    return render(request, 'eventos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect ('eventos')