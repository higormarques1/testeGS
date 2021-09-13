from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from apps.produto.forms import ProdutoForm
from apps.produto.models import Produto


@method_decorator([login_required], name='dispatch')
class CadastrarProduto(BSModalCreateView):
    """ Classe responsavel pelo cadastro do produto. """

    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('listar_produtos')
    template_name = 'cadastrar_produto.html'
    success_message = 'Produto cadastrado com sucesso!'


@method_decorator([login_required], name='dispatch')
class ListarProdutos(ListView):
    """ Classe responsavel por listar os produtos cadastrado. """

    model = Produto
    template_name = 'listar_produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10


@method_decorator([login_required], name='dispatch')
class DeletarProduto(BSModalDeleteView):
    """ Classe responsavel por realizar a exclusão do produto. """

    model = Produto
    template_name = 'deletar_produto.html'
    success_message = 'Produto deletado com sucesso!.'
    success_url = reverse_lazy('listar_produtos')


@method_decorator([login_required], name='dispatch')
class AtualizarProduto(BSModalUpdateView):
    """ Classe responsavel por atualizar os dados do produto. """

    model = Produto
    form_class = ProdutoForm
    template_name = 'atualizar_produto.html'
    success_message = 'Produto atualizado com sucesso!'


@login_required
def index(request):
    """ return: renderizar para pagina inicial. """
    return render(request, 'base.html')
