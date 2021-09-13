from bootstrap_modal_forms.forms import BSModalForm

from apps.produto.models import Produto


class ProdutoForm(BSModalForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'valor',)