from django.urls import path
from .views import CarrosAdm, CarroDeleteView, CarrosCreateView, CarroUpdateView, CarroPageAdm, ApagarUsuario, Contratos, ListarUsuarios, AtualizarUsuarioAdm, DetalharUsuario, CriarContratoAdm, DeletarContratoAdm, VerContratoAdm, AtualizarContratoAdm, DevolverCarroAdm
# from .views import Contratos

urlpatterns = [
    path('', CarrosAdm.as_view(), name='todos_os_carros'),
    path('carros/<int:id>', CarroPageAdm.as_view(), name='exibir_carro'),
    path('carros/cadastrar/', CarrosCreateView.as_view(), name='cadastrar-carro'),
    path('carros/atualizar/<int:id>', CarroUpdateView.as_view(), name='atualizar-carro'),
    path('carros/deletar/<int:id>', CarroDeleteView.as_view(), name='deletar-carro'),
    path('contratar/', CriarContratoAdm, name='contratar'),
    path('contratos/', Contratos.as_view(), name='todos_os_contratos'),
    path('detalhar_contrato/<int:id>', VerContratoAdm.as_view(), name='detalhar_contrato' ),
    path('atualizar_contrato/<int:id>', AtualizarContratoAdm.as_view(), name='atualizar_contrato' ),
    path('apagar_contrato/<int:id>', DeletarContratoAdm.as_view(), name='apagar_contrato'),
    path('devolver_carro/<int:id>', DevolverCarroAdm, name='devolver_carro'),
    path('usuarios/', ListarUsuarios.as_view(), name='todos_os_usuario'),
    path('usuarios/atualizar/<int:id>', AtualizarContratoAdm.as_view(), name='atualizar_usuario'), 
    path('usuarios/deletar/<int:id>', ApagarUsuario.as_view(), name='apagar_usuario'),
    path('detalhar/<int:id>', DetalharUsuario.as_view(), name='detalhar_usuario'),
    

    

]