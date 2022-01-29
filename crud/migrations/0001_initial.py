# Generated by Django 3.2.4 on 2021-06-23 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('rotulo', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('rotulo', models.SlugField(max_length=200)),
                ('imagem', models.ImageField(blank=True, upload_to='jogos/%Y/%m/%d/')),
                ('dispositivo', models.CharField(choices=[('PC', 'pc'), ('Console', 'console'), ('Celular', 'celular'), ('Outro', 'outro')], default='pc', max_length=20)),
                ('avaliacao', models.CharField(choices=[('Gostei', 'gostei'), ('Não gostei', 'nao gostei')], default='gostei', max_length=20)),
                ('comentario', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.categoria')),
            ],
            options={
                'ordering': ('nome',),
                'index_together': {('id', 'rotulo')},
            },
        ),
    ]