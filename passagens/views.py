from django.shortcuts import render

from passagens.forms import PassagemForm, PessoaForm


def index(request):
    form = PassagemForm()
    pessoa_form = PessoaForm()
    contexto = {'form': form, 'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        pessoa_form = PessoaForm(request.POST)
        if form.is_valid():
            contexto = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'index.html', contexto)
