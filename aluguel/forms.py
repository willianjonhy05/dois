from django.forms import ModelForm
from .models import Carro, Contrato, Usuario
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=150, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]