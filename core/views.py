from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Produto
from .forms import ProdutoForm

# View para Cadastro de Usuários (SignUp)
class CadastroUsuario(CreateView):
    """
    Controla o cadastro de novos usuários no sistema.
    Usa o formulário padrão do Django (UserCreationForm).
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redireciona para o login após criar a conta
    template_name = 'registration/signup.html'

# View para Listar Produtos (Read)
class ListarProdutos(LoginRequiredMixin, ListView):
    """
    Exibe a lista de todos os produtos cadastrados.
    Exige que o usuário esteja logado (LoginRequiredMixin).
    """
    model = Produto
    template_name = 'core/produto_list.html'
    ordering = ['nome_produto'] # Ordena a lista alfabeticamente
    login_url = 'login' # Se não estiver logado, manda para cá
    context_object_name = 'produtos' # Nome da variável para usar no template HTML

# View para Criar Produto (Create)
class CriarProduto(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário de cadastro e salva um novo produto.
    """
    model = Produto
    form_class = ProdutoForm # Usa nosso formulário com validação
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list') # Redireciona para a lista após salvar
    login_url = 'login'

# View para Editar Produto (Update)
class EditarProduto(LoginRequiredMixin, UpdateView):
    """
    Exibe o formulário preenchido e atualiza um produto existente.
    """
    model = Produto
    form_class = ProdutoForm
    template_name = 'core/produto_form.html' # Reutiliza o mesmo template de cadastro
    success_url = reverse_lazy('produto_list')
    login_url = 'login'

# View para Deletar Produto (Delete)
class DeletarProduto(LoginRequiredMixin, DeleteView):
    """
    Exibe a página de confirmação e exclui o produto.
    """
    model = Produto
    template_name = 'core/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
    login_url = 'login'
    context_object_name = 'produto' # Nome da variável para usar no template HTML
