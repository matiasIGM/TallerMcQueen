from django import forms
from django.forms import ModelForm
from .models import Vehiculo, Carrusel

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']

class CarruselForm(ModelForm):
    class Meta: 
        model = Carrusel
        fields = ['idCarrusel','enlaceImagen']
