from django.db import models

class Produto(models.Model):
    """
    Modelo que representa um Produto no banco de dados.
    Cada atributo da classe vira uma coluna na tabela.
    """
    
    # Campo de Texto (CharField) com limite de 100 caracteres
    nome_produto = models.CharField(
        max_length=100,
        verbose_name="Nome do Produto" # Nome amigável para exibição no Admin/Forms
    )
    
    # Campo Decimal para valores monetários
    # max_digits=10: Até 10 dígitos no total (ex: 12345678.90)
    # decimal_places=2: Duas casas decimais
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Preço (R$)"
    )

    def __str__(self):
        """
        Método mágico que define como o objeto é convertido para texto.
        É o que aparece no Painel Admin ou em dropdowns.
        """
        return self.nome_produto
