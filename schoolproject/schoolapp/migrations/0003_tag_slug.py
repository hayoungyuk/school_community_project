# Generated by Django 3.2.6 on 2021-08-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_remove_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, null=True, unique=True),
        ),
    ]
