# Generated by Django 3.2.6 on 2021-08-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(default='익명의 사자', max_length=100),
        ),
    ]
