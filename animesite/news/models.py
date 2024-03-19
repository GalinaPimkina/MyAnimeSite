from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    post_slug = AutoSlugField(populate_from='title', unique=True, db_index=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='news/%Y/%m/%d/', default=None, verbose_name='Обложка')
    text = models.TextField(verbose_name='Содержимое')
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='post_author', verbose_name='Автор поста')
    category = models.ManyToManyField(to='Category', related_name='post_category', verbose_name='Категория')
    tag = models.ManyToManyField(to='PostTag', related_name='post_tag', verbose_name='Тег')
    comment = models.ForeignKey(to='Comment', on_delete=models.SET_NULL, null=True, blank=True, related_name='post_comment', verbose_name='Комментарий')
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name='add_post', verbose_name='Добавлено')
    time_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования')


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='comment_author', verbose_name='Автор комментария')
    text = models.TextField(verbose_name='Текст комментария')


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    category_slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name="Слаг")


class PostTag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тег')
    tag_slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name="Слаг")
