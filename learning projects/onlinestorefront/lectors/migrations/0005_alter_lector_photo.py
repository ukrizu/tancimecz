# Generated by Django 3.2.5 on 2024-06-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0004_alter_lector_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='photo',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
