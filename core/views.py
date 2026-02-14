from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Produto
from .forms import ProdutoForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'core/produto_list.html'
    ordering = ['nome_produto']
    login_url = 'login'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list')
    login_url = 'login'

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list')
    login_url = 'login'

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'core/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
    login_url = 'login'
