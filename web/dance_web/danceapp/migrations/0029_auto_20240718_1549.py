# Generated by Django 3.2.5 on 2024-07-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0028_auto_20240718_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='lector',
        ),
        migrations.AddField(
            model_name='event',
            name='lector',
            field=models.ManyToManyField(to='danceapp.Lector'),
        ),
    ]