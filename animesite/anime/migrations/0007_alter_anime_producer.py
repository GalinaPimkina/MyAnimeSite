# Generated by Django 5.0.1 on 2024-02-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_alter_character_character_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='producer',
            field=models.ManyToManyField(blank=True, related_name='producer', to='anime.producer', verbose_name='Режиссер'),
        ),
    ]
