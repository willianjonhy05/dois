from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Carro, Usuario, Contrato

# Create your views here.


class Home(TemplateView):
    template_name="index.html"