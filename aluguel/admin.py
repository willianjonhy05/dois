from django.contrib import admin
from .models import Carro, Contrato, Usuario, Locador

# Register your models here.

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ["modelo", "ano", "placa", "diaria", "tipo", "alugado"]
    search_fields = ["modelo", "ano", "placa", "diaria", "tipo"]


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "carro", "locatario", "quantidade_de_dias", "forma_de_pagamento", "valor_total", "status"]
    search_fields = ["codigo", "carro", "locatario", "valor_total"]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "sobrenome", "email", "idade", "telefone"]
    search_fields = ["nome", "sobrenome", "email", "idade", "telefone"]

@admin.register(Locador)
class LocadorAdmin(admin.ModelAdmin):
    list_display = ["nome", "email"]
    search_fields = ["nome", "email"]