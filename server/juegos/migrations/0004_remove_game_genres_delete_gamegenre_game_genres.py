# Generated by Django 5.1.6 on 2025-02-28 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0003_game_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genres',
        ),
        migrations.DeleteModel(
            name='GameGenre',
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.CharField(default='null', max_length=15, verbose_name='genero'),
            preserve_default=False,
        ),
    ]
