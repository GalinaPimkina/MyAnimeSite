# Generated by Django 5.0.3 on 2024-03-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment_time_create_comment_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
