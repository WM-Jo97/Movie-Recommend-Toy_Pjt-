# Generated by Django 3.2 on 2022-11-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_movie_genre_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.JSONField(),
        ),
    ]