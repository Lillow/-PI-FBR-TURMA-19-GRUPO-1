from rest_framework import serializers
from .models import (
    Empresa,
    Plano,
    AreaCobertura,
    EmpresaAreaCobertura,
    Infraestrutura,
    Servico,
    Setor,
    Pessoa,
    Endereco,
)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = (
            'cnpj',
            'name',
            'razao_social',
            'sede',
            'estado',
            'ranking'
            )
        # read_only_fields = ["cnpj"] # Somente leitura


class AreaCoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCobertura
        fields = (
            'id',
          'tecnologias'
            )


class EmpresaAreaCoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaAreaCobertura
        fields = (
            'empresa_cnpj',
            'AreaCobertura_id'
            )


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = (
            'id',
            'banda',
            'empresa_cnpj'
            )


class InfraestruturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraestrutura
        fields = (
            'id',
            'asn',
            'ptt',
            'bgp',
            'operadora_backbone',
            'capacidade_backbone',
            'empresa_cnpj',
            )


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            'id',
            'tipo_plano',
            'sla',
            'preco',
            'empresa_cnpj',
            'plano_id',
            'plano_empresa_cnpj',
            )


class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = (
            'id',
            'nome'
            )


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = (
            'cpf',
            'nome',
            'cargo',
            'email',
            'telefone',
            'setor_id'
            )


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id',
            'cidade',
            'estado',
            'bairro',
            'empresa_cnpj',
            'pessoa_cpf'
            )
