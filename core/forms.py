from django import forms
from .models import Produto
import re

class ProdutoForm(forms.ModelForm):
    """
    Formulário para Criar/Editar Produtos baseados no Modelo.
    O Django cria os campos HTML automaticamente com base nos campos do Model.
    """
    class Meta:
        model = Produto
        fields = ['nome_produto', 'valor']
        
        # Widgets definem como o campo será renderizado no HTML (input text, number, etc)
        widgets = {
            'nome_produto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Camiseta Polo'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', 
                'min': '0',
                'placeholder': '0.00'
            }),
        }
        
        # Labels personalizados (rótulos acima do input)
        labels = {
            'nome_produto': 'Nome do Produto',
            'valor': 'Preço de Venda (R$)',
        }

    def clean_nome_produto(self):
        """
        Validação personalizada para o campo nome_produto.
        É chamada automaticamente quando rodamos form.is_valid().
        """
        nome = self.cleaned_data.get('nome_produto')
        
        # Validação com Regex (Expressão Regular):
        # ^ = início, $ = fim
        # [A-Za-zÀ-ÿ\s\-] = Aceita letras (incluindo acentos), espaços e hífens.
        if not re.match(r'^[A-Za-zÀ-ÿ\s\-]+$', nome):
            raise forms.ValidationError("O nome deve conter apenas letras e espaços (não aceita números ou símbolos).")
            
        return nome

    def clean_valor(self):
        """
        Validação personalizada para o campo valor.
        """
        valor = self.cleaned_data.get('valor')
        
        if valor < 0:
            raise forms.ValidationError("O valor não pode ser negativo.")
            
        return valor
