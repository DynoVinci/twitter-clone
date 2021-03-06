# Generated by Django 3.2.6 on 2021-08-27 12:09

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
