# Generated by Django 5.0.3 on 2024-03-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_category_category_slug_alter_posttag_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
