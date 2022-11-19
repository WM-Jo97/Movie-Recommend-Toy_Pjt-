# Generated by Django 3.2 on 2022-11-19 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_ids', models.JSONField()),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.TextField()),
                ('original_language', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.TextField()),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.movie')),
            ],
        ),
    ]
