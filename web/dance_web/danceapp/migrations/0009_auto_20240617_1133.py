# Generated by Django 3.2.5 on 2024-06-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0008_alter_lector_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
    ]
