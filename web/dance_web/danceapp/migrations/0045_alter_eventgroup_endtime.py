# Generated by Django 3.2.5 on 2024-08-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0044_alter_eventgroup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='endTime',
            field=models.TimeField(blank=True, default='20:00', null=True, verbose_name='Konec (nepovinné)'),
        ),
    ]