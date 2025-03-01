import uuid
from django.db import models

# Create your models here.

class Game(models.Model):

    def path_to_game(instance, filename):
        return f'juegos/{instance.id}/{filename}'

    title = models.CharField(max_length=150, verbose_name="Título")
    review = models.TextField(null=True, blank=True, verbose_name="Descripcion")
    year = models.PositiveIntegerField(default=2000, verbose_name="Año")
    video_url = models.URLField(max_length=150, null=True, blank=True, verbose_name="URL youtube")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(null=True)
    genres = models.CharField(max_length=15, verbose_name="genero")
    image_thumbnail = models.ImageField(upload_to= path_to_game, null=True, blank=True, verbose_name="Miniatura")
    image_wallpaper = models.ImageField(upload_to= path_to_game, null=True, blank=True, verbose_name="Wallpaper")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "Juego"
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.year})'
    

