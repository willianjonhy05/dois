from django.forms import ModelForm
from .models import Carro, Contrato, Usuario

class CarroForm(ModelForm):
   
    class Meta:
        model=Carro
        fields=["modelo", "ano", "placa", "foto", "cor", "diaria", "tipo"]


class UsuarioForm(ModelForm):
   
    class Meta:
        model=Usuario
        fields=["modelo", "ano", "placa", "foto", "cor", "diaria", "tipo"]
