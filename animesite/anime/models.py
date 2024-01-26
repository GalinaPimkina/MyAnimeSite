from django.db import models
from django.urls import reverse


class Anime(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name="Заголовок на русском")
    name_en = models.CharField(max_length=255, verbose_name="Заголовок на английском")
    name_jp = models.CharField(max_length=255, verbose_name="Заголовок на японском")
    genre = models.ManyToManyField(to="Genre", through="AnimeGenreTable", related_name="genre", verbose_name="Жанр")
    episodes = models.IntegerField(default=1, verbose_name="Количество эпизодов")
    year = models.ForeignKey(to="Years", on_delete=models.PROTECT, related_name="year", null=True, verbose_name="Год выхода")
    producer = models.ManyToManyField(to="Producer", through="AnimeProducerTable", related_name="producer", verbose_name="Режиссер")
    author = models.ForeignKey(to="Author", on_delete=models.PROTECT, related_name="author", verbose_name="Автор оригинала")
    tag = models.ManyToManyField(to="Tag", through="AnimeTagTable", related_query_name="tags", verbose_name="Теги")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    studio = models.ForeignKey(to="Studio", on_delete=models.PROTECT, null=True, verbose_name="Студия-издатель")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name_ru

    def get_absolute_url(self):
        return reverse('anime_page', kwargs={'anime_slug': self.slug})

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"
        ordering = ("name_ru", )


class Genre(models.Model):
    name = models.CharField(max_length=100)
    genre_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_page', kwargs={'genre_slug': self.genre_slug})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ("name", )


class AnimeGenreTable(models.Model):
    anime = models.ForeignKey(to="Anime", on_delete=models.PROTECT)
    genre = models.ForeignKey(to="Genre", on_delete=models.PROTECT)


class Years(models.Model):
    years = models.IntegerField(default=2000)

    def __str__(self):
        return str(self.years)

    def get_absolute_url(self):
        return reverse('year_page', kwargs={'year': self.years})

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Годы"
        ordering = ("years", )


class Author(models.Model):
    name = models.CharField(max_length=255)
    author_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'author_slug': self.author_slug})

    class Meta:
        verbose_name = "Автор оригинала"
        verbose_name_plural = "Авторы оригиналов"
        ordering = ("name", )


class Producer(models.Model):
    name = models.CharField(max_length=100)
    producer_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('producer_page', kwargs={'producer_slug': self.producer_slug})

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
        ordering = ("name", )


class AnimeProducerTable(models.Model):
    anime = models.ForeignKey(to="Anime", on_delete=models.PROTECT)
    producer = models.ForeignKey(to="Producer", on_delete=models.PROTECT)


class Studio(models.Model):
    name = models.CharField(max_length=100)
    studio_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studio_page', kwargs={'studio_slug': self.studio_slug})

    class Meta:
        verbose_name = "Стидия"
        verbose_name_plural = "Студии"
        ordering = ("name", )


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    tag_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag_page', kwargs={'tag_slug': self.tag_slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ("tag", )


class AnimeTagTable(models.Model):
    tag = models.ForeignKey(to="Tag", on_delete=models.PROTECT)
    anime = models.ForeignKey(to="Anime", on_delete=models.PROTECT)


class Character(models.Model):
    name = models.CharField(max_length=255)
    seiyuu = models.ForeignKey(to="Seiyuu", on_delete=models.PROTECT, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ("name", )


class Seiyuu(models.Model):
    name = models.CharField(max_length=255)
    seiyuu_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сейю"
        verbose_name_plural = "Сейю"
        ordering = ("name", )