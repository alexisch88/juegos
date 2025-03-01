# Generated by Django 5.1.6 on 2025-02-27 05:17

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=authentication.models.path_to_avatar),
        ),
    ]
