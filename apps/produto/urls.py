from django.urls import path

from apps.produto.views import AtualizarProduto, ListarProdutos, CadastrarProduto, DeletarProduto, index

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar/', CadastrarProduto.as_view(), name='cadastrar_produto'),
    path('listar/', ListarProdutos.as_view(), name='listar_produtos'),
    path('deletar/<int:pk>/', DeletarProduto.as_view(), name='deletar_produto'),
    path('atualizar/<int:pk>/', AtualizarProduto.as_view(), name='atualizar_produto'),
]
