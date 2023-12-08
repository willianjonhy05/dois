from django.forms import ModelForm
from .models import Carro, Contrato, Usuario

class CarroForm(ModelForm):
   
    class Meta:
        model=Carro
        fields=["modelo", "marca", "combustivel", "tipo", "bio", "ano", "placa", "foto", "cor", "diaria" ]


class UsuarioForm(ModelForm):
   
    class Meta:
        model=Usuario
        fields=["nome", "sobrenome", "cpfcnpj", "email", "telefone", "data_nasc", "perfil", "sexo"]

class ContratoForm(ModelForm):

    class Meta:
        Model=Contrato
        fields=["locatario", "carro", "inicio_do_contrato", "fim_do_contrato", "forma_de_pagamento"]
