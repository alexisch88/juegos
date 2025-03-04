# Generated by Django 5.1.6 on 2025-02-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'género',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('review', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('year', models.PositiveIntegerField(default=2000, verbose_name='Año')),
                ('video_url', models.URLField(blank=True, max_length=150, null=True, verbose_name='URL youtube')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(related_name='game_genres', to='juegos.gamegenre', verbose_name='Géneros')),
            ],
            options={
                'verbose_name': 'Juego',
                'ordering': ['title'],
            },
        ),
    ]
