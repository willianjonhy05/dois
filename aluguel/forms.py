from django.forms import ModelForm
from .models import Carro, Contrato, Usuario
from django.forms import ModelForm, EmailField, CharField, DateField, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

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
        model=Contrato
        fields=["locatario", "carro", "inicio_do_contrato", "fim_do_contrato", "forma_de_pagamento", "total_diarias"]
        # widgets = {
        #     'quantidade_de_dias': forms.TextInput(attrs={'readonly': 'readonly'}),
        #     'valor_total': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carro'].queryset = Carro.objects.filter(status='Disponível')


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=150, label="Email")
    cpfcnpj = CharField(max_length=18, label="CPF/CNPJ")
    telefone = CharField(max_length=20, label="Telefone")
    data_nasc = DateField(label="Data de Nascimento")
    perfil = ImageField(label="Foto")


    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'cpfcnpj', 'telefone' , 'data_nasc', 'perfil', 'email', 'password1', 'password2' ]