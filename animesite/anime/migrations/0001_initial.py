# Generated by Django 5.0.1 on 2024-01-10 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('producer_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seiyuu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('seiyuu_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studio_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('tag_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('name_jp', models.CharField(max_length=255)),
                ('episodes', models.IntegerField(default=1)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to='anime.author')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeGenreTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.anime')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.genre')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(related_name='genre', through='anime.AnimeGenreTable', to='anime.genre'),
        ),
        migrations.CreateModel(
            name='AnimeProducerTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.anime')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.producer')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='producer',
            field=models.ManyToManyField(related_name='producer', through='anime.AnimeProducerTable', to='anime.producer'),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('seiyuu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='anime.seiyuu')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='anime.studio'),
        ),
        migrations.CreateModel(
            name='AnimeTagTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.anime')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.tag')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='tag',
            field=models.ManyToManyField(related_query_name='tags', through='anime.AnimeTagTable', to='anime.tag'),
        ),
        migrations.AddField(
            model_name='anime',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='year', to='anime.years'),
        ),
    ]
