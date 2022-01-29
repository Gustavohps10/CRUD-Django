from django.contrib import admin
from .models import Categoria, Jogo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rotulo']
    prepopulated_fields = {'rotulo': ('nome',)}

@admin.register(Jogo)
class CategoriaJogo(admin.ModelAdmin):
    list_display = ['nome', 'rotulo', 'categoria', 'dispositivo', 'avaliacao', 'comentario']
    prepopulated_fields = {'rotulo': ('nome',)}
