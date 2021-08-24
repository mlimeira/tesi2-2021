from django.contrib import messages
from django.shortcuts import render
from app1.forms import ClienteModelForm


# Create your views here.
def pagina_principal(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

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