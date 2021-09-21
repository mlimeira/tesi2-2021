from django.contrib import messages
from django.shortcuts import render, redirect
from app1.forms import ClienteModelForm, ContatoModelForm, ProdutoModelForm, PedidoModelForm
from app1.models import Produto

# Create your views here.
def pagina_principal(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato cadastrado com sucesso!')
            form = ContatoModelForm()
        else:
            messages.error(request, 'Contato não cadastrado!')
    else:
        form = ContatoModelForm()

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def cliente(request):
    if request.method == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            form = ClienteModelForm()
        else:
            messages.error(request, 'Cliente não cadastrado!')
    else:
        form = ClienteModelForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'cliente.html', context)

def produto(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto cadastrado com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Produto não cadastrado!')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('produto_list')

def produto_list(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto_list.html', context)

def pedido(request):
    if request.method == 'POST':
        form = PedidoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            form = PedidoModelForm()
        else:
            messages.error(request, 'Cliente não cadastrado!')
    else:
        form = PedidoModelForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'pedido.html', context)