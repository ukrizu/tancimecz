# Generated by Django 3.2.5 on 2024-06-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0022_rename_adress_location_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
