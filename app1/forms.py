from django import forms
from app1.models import Cliente, Contato, Produto, Pedido

class ClienteModelForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['contato', 'nome', 'sobrenome', 'email']

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['telefone']

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'imagem']

class PedidoModelForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produto']