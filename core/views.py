from core.forms import VehiculoForm
from django import forms
from django.shortcuts import render, redirect
from .models import Carrusel, Mecanicos
# Create your views here.
def home(request):
    imagenesCarrusel = Carrusel.objects.all()
    mecanicos = Mecanicos.objects.all()
    datos = {
        'imagenesCarrusel': imagenesCarrusel ,
        'perfilMecanicos' : mecanicos
    }

    return render(request,'core/home.html',datos)



def listaseries(request):
    lista = ["Jujustsu Kaisen","Dragon Ball Z","Boku no hero academia"]
    contexto = {"nombre":"Los Venegas","series":lista}
    return render(request,'core/listaseries.html',contexto)

def form_vehiculo(request):
    datos = {
        'form': VehiculoForm
    }
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request,'core/form_vehiculo.html',datos)

def form_mod_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente = id)
    datos = {
        'form':VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"

    return render(request,'core/form_mod_vehiculo.html',datos)

def form_del_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente = id)
    vehiculo.delete()
    return redirect(to="home")

