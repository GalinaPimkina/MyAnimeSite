# Generated by Django 5.0.3 on 2024-03-19 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст комментария'),
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_comment', to='news.comment', verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='posttag',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
        ),
    ]
