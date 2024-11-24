from rest_framework import generics, mixins, viewsets
from .models import Empresa, AreaCobertura, Plano, Setor, Infraestrutura, Servico, Pessoa, Endereco, EmpresaAreaCobertura
from .serializers import EmpresaSerializer, AreaCoberturaSerializer, PlanoSerializer, SetorSerializer, InfraestruturaSerializer, ServicoSerializer, PessoaSerializer, EnderecoSerializer, EmpresaAreaCoberturaSerializer


class EmpresaAPIViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class AreaCoberturaAPIViewSet(viewsets.ModelViewSet):
    queryset = AreaCobertura.objects.all()
    serializer_class = AreaCoberturaSerializer

class PlanoAPIViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

class SetorAPIViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class InfraestruturaAPIViewSet(viewsets.ModelViewSet):
    queryset = Infraestrutura.objects.all()
    serializer_class = InfraestruturaSerializer

class ServicoAPIViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class PessoaAPIViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class EnderecoAPIViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
class EmpresaAreaCoberturaAPIViewSet(viewsets.ModelViewSet):
    queryset = EmpresaAreaCobertura.objects.all()
    serializer_class = EmpresaAreaCoberturaSerializer