# Generated by Django 3.2.5 on 2024-06-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='photo',
            field=models.ImageField(upload_to='staticfiles'),
        ),
    ]
