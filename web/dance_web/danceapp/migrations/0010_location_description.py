# Generated by Django 3.2.5 on 2024-06-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0009_auto_20240617_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
