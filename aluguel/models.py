from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

# Create your models here.

# Dados para registro da classe Carro

class Carro(models.Model):

    CATEGORIAS = [
        ("Econômico", "Econômico"),
        ("Intermediário", "Intermediário"),
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Executivo", "Executivo"),
        ("Pick-UP", "Pick-UP"),
        ("Minivan", "Minivan"),
    ]

    COMBUSTIVEL = [
        ("Gasolina", "Gasolina"),
        ("Flex", "Flex"),
        ("Diesel", "Diesel"),
        ("Híbrido", "Híbrido"),
        ("Elétrico", "Elétrico"),

    ]

    STATUS = [
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível'),
    ]

    MARCA = [
        ('Mercedes - Benz', 'Mercedes - Benz'), ('Audi', 'Audi'),('BMW', 'BMW'),
        ('Volkswagen',  'Volkswagen'), ('Chevrolet', 'Chevrolet'), ('Renault', 'Renault'),
        ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Fiat', 'Fiat'), ('Hyundai', 'Hyundai'),
        ('Peugeot', 'Peugeot'), ('Lexus', 'Lexus'), ('Kia','Kia'), ('Citroën', 'Citroën'),
        ('Nissan', 'Nissan'), ('Mitsubishi', 'Mitsubishi'), ('Chery', 'Chery'),('Jeep', 'Jeep'),
    ]

    modelo = models.CharField("Modelo", max_length=50)
    marca = models.CharField("Marca", choices=MARCA, max_length=50)
    combustivel = models.CharField("Combustível", max_length=50, choices=COMBUSTIVEL)
    tipo = models.CharField("Categoria", max_length=100, choices=CATEGORIAS)
    bio = models.TextField("Sobre o carro", blank=True, null=True)
    ano = models.PositiveIntegerField("Ano")
    placa = models.CharField(max_length=15, unique=True, error_messages={'unique':"Veículo já cadastrado!"})
    foto = models.ImageField("Foto", upload_to='carros/', blank=True, null=True)
    cor = models.CharField("Cor", max_length=50)
    diaria = models.DecimalField("Valor da diária", max_digits=8, decimal_places=2)    
    status = models.CharField(max_length=12, choices=STATUS, default='Disponível')


    def __str__(self):
       return f"{self.modelo} - {self.placa} - {self.status}"
    
    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


class Usuario(models.Model):

    SEXO = [
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("Outro", "Outro")
    ]


    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    cpfcnpj = models.CharField('CPF:',max_length=18)
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=20)
    data_nasc = models.DateField("Data de Nascimento")
    perfil = models.ImageField("Foto", upload_to='perfil', blank=True, null=True)
    user = models.OneToOneField(get_user_model(),verbose_name="Usuário:", on_delete=models.CASCADE, blank=True, null=True)

    def calculo_de_idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nasc
        return round(diferenca.days // 365.25)

    idade = property(calculo_de_idade)
    sexo = models.CharField("Sexo", max_length=100, choices=SEXO)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.email} - {self.idade}'
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Locador(models.Model):
    nome = models.CharField("Nome", max_length=200)
    email = models.EmailField("Email")
    avatar = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)
   

    def __str__(self):
        return self.nome + " " + self.email
    
    class Meta:
        verbose_name = "Locador"
        verbose_name_plural = "Locadores"

class Contrato(models.Model):

    FORMA = [
        ("Crédito", "Crédito"),
        ("Débito", "Débito"),
        ("Boleto", "Boleto"),
        ("PIX", "PIX"),
        ("Transferência", "Transferência"),
        ("Espécie", "Espécie"),
        ("Outro", "Outro"),

    ]

    ANDAMENTO = [
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),

    ]

    
    locatario = models.ForeignKey(Usuario, verbose_name="Locatário", on_delete=models.CASCADE, related_name="contratante")
    carro = models.ForeignKey(Carro, verbose_name="Veículo", on_delete=models.CASCADE, related_name='Veículo')
    inicio_do_contrato = models.DateField("Data de Retirada do Carro")
    fim_do_contrato = models.DateField("Data da Devolução do Carro")

    def calcular_dias(self):
        return (self.fim_do_contrato - self.inicio_do_contrato).days

    quantidade_de_dias = property(calcular_dias)
    forma_de_pagamento = models.CharField("Forma de Pagamento", max_length=100, choices=FORMA)

    def calcular_valor(self):
        valor = self.quantidade_de_dias * self.carro.diaria
        return valor

    valor_total = property(calcular_valor)
    status = models.CharField(max_length=12, choices=ANDAMENTO, default='Ativo')

    def __str__(self):
       return f"{self.carro.modelo} - {self.locatario.nome} - {self.quantidade_de_dias} - {self.valor_total}"
    
    # def save(self, *args, **kwargs):
    #     if self.carro.status == 'Disponível':
    #         self.carro.status = 'Indisponível'
    #     else:
    #         self.carro.status = 'Disponível'
    
    
    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"