# Generated by Django 3.2 on 2022-11-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.TextField(null=True),
        ),
    ]