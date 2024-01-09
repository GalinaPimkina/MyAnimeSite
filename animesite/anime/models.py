from django.db import models

class Anime(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_jp = models.CharField(max_length=255)
    genre = models.ManyToManyField(to="Genre", through="AnimeGenreTable", related_name="genre")
    episodes = models.IntegerField(default=1)
    year = models.ForeignKey(to="Years", on_delete=models.PROTECT, related_name="year", null=True)
    producer = models.ManyToManyField(to="Producer", through="AnimeProducerTable", related_name="producer")
    author = models.ForeignKey(to="Author", on_delete=models.PROTECT, related_name="author")
    tag = models.ManyToManyField(to="AnimeTag", through="AnimeTagTable", related_query_name="tags")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    studio = models.ForeignKey(to="Studio", on_delete=models.PROTECT, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name_ru


class Genre(models.Model):
    name = models.CharField(max_length=100)
    genre_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class AnimeGenreTable(models.Model):
    anime = models.ForeignKey(to="Anime", on_delete=models.PROTECT)
    genre = models.ForeignKey(to="Genre", on_delete=models.PROTECT)


class Years(models.Model):
    years = models.IntegerField(default=2000)

    def __str__(self):
        return str(self.years)


class Author(models.Model):
    name = models.CharField(max_length=255)
    author_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=100)
    producer_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name