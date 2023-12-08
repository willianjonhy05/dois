from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Carro, Usuario, Contrato
from django.urls import reverse
from .forms import CarroForm
from django.contrib import messages
# Create your views here.

# Views Públicas - São Responsáveis para visualização do Público Geral // Sem necessidade de Login


class Home(TemplateView):
    template_name="index.html"

class CarrosListView(ListView):
    model=Carro
    template_name='carros.html'
    context_object_name='carros'
    paginate_by = 5

class CarroPage(DetailView):
    model=Carro
    template_name='carro.html'
    context_object_name='carro'
    pk_url_kwarg='id'

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

# Views Limitadas - São Responsáveis para visualização limitadas ao usuário/cliente // Com necessidade de Login

