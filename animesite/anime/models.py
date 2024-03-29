from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Anime(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name="Заголовок на русском")
    name_en = models.CharField(max_length=255, verbose_name="Заголовок на английском")
    name_jp = models.CharField(max_length=255, verbose_name="Заголовок на японском")
    anime_slug = AutoSlugField(populate_from='name_jp', unique=True, db_index= True, verbose_name="Слаг")
    image = models.ImageField(upload_to="image/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Обложка")
    genre = models.ManyToManyField("Genre", related_name="genre", verbose_name="Жанр")
    episodes = models.IntegerField(default=1, verbose_name="Количество эпизодов")
    year = models.ForeignKey(to="Years", on_delete=models.PROTECT, related_name="years", verbose_name="Год выхода")
    producer = models.ManyToManyField("Producer", blank=True, related_name="producer", verbose_name="Режиссер")
    author = models.ForeignKey(to="Author", on_delete=models.PROTECT, related_name="author", verbose_name="Автор оригинала")
    tag = models.ManyToManyField("Tag", related_name="tags", verbose_name="Теги")
    studio = models.ManyToManyField("Studio", related_name="studio", verbose_name="Студия-издатель")
    description = models.TextField(verbose_name="Описание")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_anime", verbose_name="Добавлено")

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"
        ordering = ("name_ru", )

    def __str__(self):
        return self.name_ru

    def get_absolute_url(self):
        return reverse('anime_page', kwargs={'anime_slug': self.anime_slug})


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")
    genre_slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_genre", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime_from_genre_page', kwargs={'genre_slug': self.genre_slug})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ("name", )


class Years(models.Model):
    year = models.IntegerField(default=2000, verbose_name="Год издания")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_year", verbose_name="Добавлено")

    def __str__(self):
        return str(self.year)

    def get_absolute_url(self):
        return reverse('anime_from_year_page', kwargs={'year': self.year})

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Годы"
        ordering = ("year", )


class Author(models.Model):
    name = models.CharField(max_length=255,  verbose_name="Имя")
    author_slug = AutoSlugField(populate_from="name", unique=True, db_index=True,  verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_author", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime_from_author_page', kwargs={'author_slug': self.author_slug})

    class Meta:
        verbose_name = "Автор оригинала"
        verbose_name_plural = "Авторы оригиналов"
        ordering = ("name", )


class Producer(models.Model):
    name = models.CharField(max_length=100,  verbose_name="Имя")
    producer_slug = AutoSlugField(populate_from="name", unique=True, db_index=True,  verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_producer", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime_from_producer_page', kwargs={'producer_slug': self.producer_slug})

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
        ordering = ("name", )


class Studio(models.Model):
    name = models.CharField(max_length=100,  verbose_name="Название")
    studio_slug = AutoSlugField(populate_from="name", unique=True, db_index=True,  verbose_name="Слаг")
    logo = models.ImageField(upload_to="logo/%Y/%m/%d/", verbose_name="Логотип")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None,  related_name="add_studio", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime_from_studio_page', kwargs={'studio_slug': self.studio_slug})

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"
        ordering = ("name", )


class Tag(models.Model):
    tag = models.CharField(max_length=100,  verbose_name="Teг")
    tag_slug = AutoSlugField(populate_from="tag", unique=True, db_index=True,  verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_tag", verbose_name="Добавлено")

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('anime_from_tag_page', kwargs={'tag_slug': self.tag_slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ("tag", )


class Character(models.Model):
    name = models.CharField(max_length=255,  verbose_name="Имя")
    seiyuu = models.ForeignKey(to="Seiyuu", on_delete=models.PROTECT, verbose_name="Слаг")
    description = models.TextField()
    character_slug = AutoSlugField(populate_from="name", unique=True, db_index=True, verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_character", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ("name", )


class Seiyuu(models.Model):
    name = models.CharField(max_length=255,  verbose_name="Имя")
    seiyuu_slug = AutoSlugField(populate_from="name", unique=True, db_index=True,  verbose_name="Слаг")
    action = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="add_seiyuu", verbose_name="Добавлено")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сейю"
        verbose_name_plural = "Сейю"
        ordering = ("name", )