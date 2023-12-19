from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Carro, Usuario, Contrato
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from .forms import CarroForm, RegistrationForm, ContratoForm, UsuarioForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# Views Públicas - São Responsáveis para visualização do Público Geral // Sem necessidade de Login


class Home(TemplateView):
    template_name="index.html"

class CarrosListView(ListView):
    model=Carro
    template_name='carros.html'
    context_object_name='carros'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get("busca")

        if search:
            self.carros = Carro.objects.filter(modelo__icontains=search)
        else:
            self.carros = Carro.objects.all()

        return self.carros

class CarroPage(DetailView):
    model=Carro
    template_name='carro.html'
    context_object_name='carro'
    pk_url_kwarg='id'

class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')


class CriarUsuario(CreateView):
    model = Usuario
    template_name = 'criar_usuario.html'
    form_class = UsuarioForm
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Usuário cadastrado com sucesso!")
        return reverse('home')


# Views Privadas - São Responsáveis para visualização restritas do admin // Com necessidade de Login

class CarrosAdm(ListView):
    model=Carro
    template_name='locador/todos_carros.html'
    context_object_name='carros'

class CarrosCreateView(CreateView):
    model=Carro
    template_name='locador/cadastrar_carro.html'
    form_class=CarroForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro cadastrado com sucesso!")
        return reverse('todos_os_carros')
    
class CarroUpdateView(UpdateView):
    model=Carro
    template_name='locador/atualizar_carro.html'
    form_class=CarroForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizado com sucesso!")
        return reverse('todos_os_carros')
    
class CarroDeleteView(DeleteView):
    model=Carro
    template_name='locador/apagar_carro.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro apagado com sucesso!")
        return reverse('todos_os_carros')
    
class CarroPageAdm(DetailView):
    model=Carro
    template_name='locador/sobre_o_carro.html'
    context_object_name='carro'
    pk_url_kwarg='id'

class ListarUsuarios(ListView):
    model=Usuario
    template_name='locador/usuarios.html'
    context_object_name='usuarios'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get("busca")

        if search:
            self.usuarios = Usuario.objects.filter(nome__icontains=search)
        else:
            self.usuarios = Usuario.objects.all()

        return self.usuarios


class ApagarUsuario(DeleteView):
    model=Usuario
    template_name='locador/apagar_usuario.html'
    pk_url_kwarg='id'

class AtualizarUsuarioAdm(UpdateView):
    model=Usuario
    template_name='locador/atualizar_usuario.html'
    form_class=UsuarioForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Usuário atualizado com sucesso!")
        return reverse('todos_os_usuario')
    

class DetalharUsuario(DetailView):
    model=Usuario
    template_name='locador/detalhar_usuario.html'
    context_object_name='usuario'
    pk_url_kwarg='id'


# class Contratos(ListView):
#     model=Contrato
#     template_name='locador/todos_os_contratos.html'
#     context_object_name='contratos'




# Views Limitadas - São Responsáveis para visualização limitadas ao usuário/cliente // Com necessidade de Login

class PerfilUsuario(DetailView):
    model=Usuario
    template_name='usuario/meu_perfil.html'
    context_object_name='usuario'
    pk_url_kwarg='id'

class AtualizarUsuario(UpdateView):
    model=Usuario
    template_name='usuario/atualizar_usuario.html'
    form_class=UsuarioForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Perfil atualizado com sucesso!")
        return reverse('home')


def alugar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    
    if request.method == 'POST':
        form = ContratoForm(request.POST, initial={'carro': carro})
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.carro = carro
            contrato.save()
            return redirect('lista_de_carros')
    else:
        form = ContratoForm()

    return render(request, 'usuario/alugar_carro.html', {'carro': carro, 'form': form})

# def Criar_Contrato(request):
#     if request.method =='POST':
#         form = ContratoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             carro = Carro.objects.get(id=int(request.POST.get('carro'))) 
#             carro.status = 'Indisponível'
#             carro.save()
#             messages.success(request, 'Contrato realizado com sucesso!')
#             return redirect('lista_de_carros')
        
#         else:
#             form = ContratoForm()
#             return render(request, 'usuario/contratar_carro.html', {'form':form})
    
# def Criar_Contrato(request):
#     if request.method == 'POST':
#         form = ContratoForm(request.POST)
#         if form.is_valid():
#             contrato = form.save()
#             carro_id = int(request.POST.get('carro'))
#             carro = Carro.objects.get(id=carro_id)
#             carro.status = 'Indisponível'
#             carro.save()
#             messages.success(request, 'Contrato realizado com sucesso!')
#             return redirect('lista_de_carros')
#     else:
#         form = ContratoForm()

#     return render(request, 'usuario/contratar_carro.html', {'form': form})

class CriarContrato(CreateView):
    model=Contrato
    template_name='usuario/contratar_carro.html'
    form_class=ContratoForm
    success_url = 'confirmar-contrato'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contrato cadastrado com sucesso!")
        return reverse('lista_de_carros')
    
    def form_valid(self, form):        
        form.instance.quantidade_de_dias = (form.instance.fim_do_contrato - form.instance.inicio_do_contrato).days
        form.instance.valor_total = form.instance.calcular_valor()
        return super().form_valid(form)
    

class DevolverCarro(UpdateView):
    model=Contrato
    template_name='usuario/devolver_carro.html'
    form_class=ContratoForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contrato cadastrado com sucesso!")
        return reverse('lista_de_carros')
    
    def form_valid(self, form):        
        form.instance.quantidade_de_dias = (form.instance.fim_do_contrato - form.instance.inicio_do_contrato).days
        form.instance.valor_total = form.instance.calcular_valor()
        return super().form_valid(form)
    


    
#     def form_valid(self, form):
#         carro_id = form.cleaned_data['carro'].id
#         carro = get_object_or_404(Carro, pk=carro_id)
#         response = super().form_valid(form)
#         carro.status = 'Indisponível'
#         carro.save()
#         contrato = form.save(commit=False)
#         contrato.valor_total = contrato.calcular_valor()
#         contrato.save()    
#         return render(self.request, 'usuario/confirmar_contrato.html', {'contrato': contrato})
    
# def confirmar_contrato(request):
#     if request.method == 'POST' and request.POST.get('confirma_contrato') == 'confirmar':
#         # Aqui você pode realizar ações adicionais, como enviar um e-mail de confirmação, etc.
#         return render(request, 'contrato_confirmado.html')
#     else:
#         return redirect('contratar-carro')  # Redireciona de volta para a página de criar contrato se não confirmar

        
        # messages.add_message(self.request, messages.SUCCESS, "Contrato de aluguel cadastrado com sucesso!")
        
        # carro.status = 'Indisponível'
        # carro.save()
        # return response






# class CriarContrato(CreateView):
#     model=Contrato
#     template_name='usuario/contratar_carro.html'
#     form_class=ContratoForm

#     def get_success_url(self):
#         messages.add_message(self.request, messages.SUCCESS, "Carro alugado com sucesso!")
#         return reverse('meus_contratos')


# class MeusContratos(ListView):
#     model=Contrato
#     template_name='usuario/todos_carros.html'
#     context_object_name='carros'

