# Generated by Django 4.1 on 2024-02-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0013_rename_slug_anime_anime_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/%Y/%m/%d/', verbose_name='Обложка'),
        ),
    ]
