from .models import Jogo, Categoria
from django import forms


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'rotulo']

class FormularioJogo(forms.ModelForm):
    class Meta:
        model = Jogo
        fields =  ['nome', 'rotulo','imagem', 'categoria', 'dispositivo', 'avaliacao', 'comentario']
       