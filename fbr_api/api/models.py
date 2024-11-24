from django.db import models


class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, unique=True, primary_key=True)
    name = models.CharField(max_length=45)
    razao_social = models.CharField(max_length=45)  # Nome jurídico de uma empresa
    sede = models.CharField(
        max_length=45
    )  # Local oficial onde a organização está localizada
    estado = models.CharField(max_length=45)  # Porque não ser 2 caracteres?
    ranking = models.CharField(max_length=45)  # Quais os valores possíveis

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"

    def __str__(self):
        return str(self.cnpj)



class AreaCobertura(models.Model):
    id = models.AutoField(unique=True, primary_key=True, auto_created=True)
    tecnologias = models.CharField(max_length=45)

    class Meta:
        verbose_name = "area de cobertura"
        verbose_name_plural = "areas de cobertura"

    def __str__(self):
        return str(self.id)


class EmpresaAreaCobertura(models.Model):
    empresa_cnpj = models.ForeignKey(
        Empresa, related_name="area_empresa_cnpj", on_delete=models.CASCADE
    )
    AreaCobertura_id = models.ForeignKey(
        AreaCobertura, related_name="area_cobertura_id", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "empresa-area de cobertura"


class Plano(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    banda = models.CharField(max_length=45)
    empresa_cnpj = models.ForeignKey(
        Empresa, related_name="plano_empresa_cnpj", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "plano"
        verbose_name_plural = "planos"

    def __str__(self):
        return str(self.id)


class Infraestrutura(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    asn = models.CharField(max_length=45)
    ptt = models.CharField(max_length=45)
    bgp = models.CharField(max_length=45)
    operadora_backbone = models.CharField(max_length=45)
    capacidade_backbone = models.CharField(max_length=45)
    empresa_cnpj = models.ForeignKey(
        Empresa, related_name="infra_empresa_cnpj", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "infraestrutura"
        verbose_name_plural = "infraestruturas"

    def __str__(self):
        return str(self.id)


class Servico(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    tipo_plano = models.CharField(max_length=45)
    sla = models.CharField(max_length=45)
    preco = models.IntegerField()
    empresa_cnpj = models.ForeignKey(
        Empresa, related_name="servico_empresa_cnpj", on_delete=models.CASCADE
    )
    plano_id = models.ForeignKey(
        Plano, related_name="servico_plano_id", on_delete=models.CASCADE
    )
    plano_empresa_cnpj = models.ForeignKey(
        Plano, related_name="servico_plano_empresa_cnpj", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "serviço"
        verbose_name_plural = "serviços"

    def __str__(self):
        return str(self.id)


class Setor(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    nome = models.CharField(max_length=45)

    class Meta:
        verbose_name = "setor"
        verbose_name_plural = "setores"

    def __str__(self):
        return str(self.id)


class Pessoa(models.Model):
    cpf = models.CharField(max_length=45, unique=True, primary_key=True)
    nome = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    telefone = models.CharField(max_length=45)
    setor_id = models.ForeignKey(
        Setor, related_name="pessoa_setor_id", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "pessoa"
        verbose_name_plural = "pessoas"

    def __str__(self):
        return self.cpf


class Endereco(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    estado = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    empresa_cnpj = models.ForeignKey(
        Empresa, related_name="endereco_empresa_cnpj", on_delete=models.CASCADE
    )
    pessoa_cpf = models.ForeignKey(
        Pessoa, related_name="endereco_pessoa_cpf", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "endereco"
        verbose_name_plural = "enderecos"

    def __str__(self):
        return str(self.id)
