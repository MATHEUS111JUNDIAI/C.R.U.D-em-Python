from django.urls import path
from .views import ListarProdutos, CriarProduto, EditarProduto, DeletarProduto, CadastroUsuario

urlpatterns = [
    # Rota Inicial (Lista de Produtos)
    path('', ListarProdutos.as_view(), name='produto_list'),
    
    # Rotas de CRUD
    path('novo/', CriarProduto.as_view(), name='produto_create'),
    path('editar/<int:pk>/', EditarProduto.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', DeletarProduto.as_view(), name='produto_delete'),
    
    # Rota de Cadastro de Usuário
    path('signup/', CadastroUsuario.as_view(), name='signup'),
]
