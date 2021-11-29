from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker

from .models.pessoa import Pessoa
from .models.passagem import Passagem
from .classe_viagem import tipos_de_classe
from .validation import *


class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Pesquisa', widget=DatePicker(), disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe do Vôo',
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        data_ida = self.cleaned_data.get('data_ida')
        destino = self.cleaned_data.get('destino')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_maior_que_hoje(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
