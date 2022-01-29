from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('cadastrar/jogo/', views.cadastrarJogo, name = "cadastrarJogo"),
    path('cadastrar/categoria/', views.cadastrarCategoria, name = "cadastrarCategoria"),
    path('listar/categoria', views.listarCategorias, name = "listarCategorias"),
    path('', views.listarJogos, name="listarJogos"),
    path('deletarCategoria/<int:id>', views.deletarCategoria, name='deletarCategoria'),
    path('deletarJogo/<int:id>', views.deletarJogo, name='deletarJogo'),
    path('<slug:rotuloCategoria>/', views.listarJogos, name = "listarJogosCategoria"),
    path('editar/jogo/<int:id>', views.editarJogo, name='editarJogo'),
    path('editar/categoria/<int:id>', views.editarCategoria, name='editarCategoria'),
    path('<int:id>/<slug:rotulo>/', views.detalharJogo, name = "detalharJogo"),
   
]