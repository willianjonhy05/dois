from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Carro, Usuario, Contrato

# Create your views here.


class MidiaCreateView(CreateView):
    model=Carro
    template_name='midias/cadastrar.html'
    form_class=MidiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme/Série cadastrado com sucesso!")
        return reverse('listar-midias')