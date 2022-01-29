from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    rotulo = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("crud:listarJogosCategoria", args=[self.rotulo])

class Jogo(models.Model):
    AVALIACAO_CHOICES = [
        ('Gostei', 'gostei'),
        ('Não gostei', 'nao gostei'),
    ]
    DISPOSITIVO_CHOICES = [
        ('PC', 'pc'),
        ('Console', 'console'),
        ('Celular', 'celular'),
        ('Outro', 'outro'),
    ]
    nome = models.CharField(max_length=200, db_index=True)
    rotulo = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='jogos/%Y/%m/%d/', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dispositivo = models.CharField(max_length=20, choices=DISPOSITIVO_CHOICES, default='pc')
    avaliacao =  models.CharField(max_length=20, choices=AVALIACAO_CHOICES, default='gostei')
    comentario = models.TextField()
 
    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'rotulo'),)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("crud:detalharJogo", args=[self.id, self.rotulo])
