# Generated by Django 3.2.5 on 2024-06-14 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0006_alter_lector_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
