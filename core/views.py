from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'core/produto_list.html'
    ordering = ['nome_produto'] # Ordenação padrão

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm # Usa o formulário com validação
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm # Usa o formulário com validação
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'core/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
