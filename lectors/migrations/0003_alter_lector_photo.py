# Generated by Django 3.2.5 on 2024-06-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0002_alter_lector_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='photo',
            field=models.ImageField(upload_to='C:\\Annie\\Django\\learning projects\\onlinestorefront\\staticfiles'),
        ),
    ]
