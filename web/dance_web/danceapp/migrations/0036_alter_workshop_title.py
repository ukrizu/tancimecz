# Generated by Django 3.2.5 on 2024-07-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0035_auto_20240727_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(max_length=101, verbose_name='Název'),
        ),
    ]