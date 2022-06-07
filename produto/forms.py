from django import forms
from produto.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','quantidade','preco','imagem','Status']