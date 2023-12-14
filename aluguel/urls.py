from django.urls import path
from .views import CarrosAdm, CarroDeleteView, CarrosCreateView, CarroUpdateView, CarroPageAdm, ApagarUsuario, ListarUsuarios, AtualizarUsuarioAdm
# from .views import Contratos

urlpatterns = [
    path('', CarrosAdm.as_view(), name='todos_os_carros'),
    path('carros/<int:id>', CarroPageAdm.as_view(), name='exibir_carro'),
    path('carros/cadastrar/', CarrosCreateView.as_view(), name='cadastrar-carro'),
    path('carros/atualizar/<int:id>', CarroUpdateView.as_view(), name='atualizar-carro'),
    path('carros/deletar/<int:id>', CarroDeleteView.as_view(), name='deletar-carro'),
    # path('contratos/', Contratos.as_view(), name='todos_os_contratos'),
    path('usuarios/', ListarUsuarios.as_view(), name='todos_os_usuario'),
    path('usuarios/atualizar/<int:id>', AtualizarUsuarioAdm.as_view(), name='atualizar_usuario'), 
    path('usuarios/deletar/<int:id>', ApagarUsuario.as_view(), name='apagar_usuario'),
    

    

]