# Generated by Django 3.2.5 on 2024-06-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0002_auto_20240612_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]