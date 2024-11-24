from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    EmpresaAPIViewSet, 
    PlanoAPIViewSet,
    SetorAPIViewSet,
    PessoaAPIViewSet,
    InfraestruturaAPIViewSet,
    AreaCoberturaAPIViewSet,
    EnderecoAPIViewSet, 
    EmpresaAreaCoberturaAPIViewSet,
    ServicoAPIViewSet
       
)
router = DefaultRouter()
router.register('empresa', EmpresaAPIViewSet, basename='empresa')
router.register('plano', PlanoAPIViewSet, basename= 'plano')
router.register('setor', SetorAPIViewSet, basename='setor' )
router.register('pessoa',PessoaAPIViewSet,basename='pessoa')
router.register('infraestrutura', InfraestruturaAPIViewSet,basename='infraestrutura')
router.register('area-cobertura', AreaCoberturaAPIViewSet, basename='area-de-cobertura')
router.register('endereco',EnderecoAPIViewSet, basename= 'endereco')
router.register('empresa-area-cobertura', EmpresaAreaCoberturaAPIViewSet, basename= 'empresa-na-area-de-cobertura')
router.register('servico', ServicoAPIViewSet, basename='servico')

urlpatterns = [
       
]
