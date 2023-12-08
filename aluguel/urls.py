from django.urls import path
from .views import CarrosAdm, CarroDeleteView, CarrosCreateView, CarroUpdateView, CarroPageAdm

urlpatterns = [
    path('carros/', CarrosAdm.as_view(), name='todos_os_carros'),
    path('carros/<int:id>', CarroPageAdm.as_view(), name='exibir_carro'),
    path('carros/cadastrar/', CarrosCreateView.as_view(), name='cadastrar-carro'),
    path('carros/atualizar/<int:id>', CarroUpdateView.as_view(), name='atualizar-carro'),
    path('carros/deletar/<int:id>', CarroDeleteView.as_view(), name='deletar-carro'),
    

]