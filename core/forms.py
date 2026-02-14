from django import forms
from .models import Produto
import re

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'valor']
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Camiseta Polo'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }
        labels = {
            'nome_produto': 'Nome do Produto',
            'valor': 'Preço (R$)',
        }

    def clean_nome_produto(self):
        nome = self.cleaned_data.get('nome_produto')
        # Regex: Permite letras, números, espaços e hífen. Bloqueia outros caracteres especiais.
        if not re.match(r'^[A-Za-z0-9\s\-]+$', nome):
            raise forms.ValidationError("O nome deve conter apenas letras, números e espaços (sem caracteres especiais).")
        return nome

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor < 0:
            raise forms.ValidationError("O valor não pode ser negativo.")
        return valor
