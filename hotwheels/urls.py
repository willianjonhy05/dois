"""
URL configuration for hotwheels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aluguel.views import Home, CarrosListView, CarroPage, RegistrationView, CriarUsuario, PerfilUsuario, AtualizarUsuario, CriarContrato, alugar_carro

urlpatterns = [    
    path('', Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', RegistrationView.as_view(), name='registration'),    
    path('locador/', include('aluguel.urls')),
    path('carros/', CarrosListView.as_view(), name='lista_de_carros'),
    path('contratar/', CriarContrato.as_view(), name='contratar-carro'),
    # path('confirmar_contrato/', confirmar_contrato, name='confirma_contrato'),
    path('alugar_carro/<int:carro_id>/', alugar_carro, name='alugar_carro'),
    path('carro/<int:id>', CarroPage.as_view(), name='detalhar-carro'),
    path('novo_usuario/', CriarUsuario.as_view(), name='novo-usuario'),
    path('meu_perfil/<int:id>', PerfilUsuario.as_view(), name='meu-perfil'),   
    path('usuario/atualizar/<int:id>', AtualizarUsuario.as_view(), name='atualizar-usuario'), 
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
