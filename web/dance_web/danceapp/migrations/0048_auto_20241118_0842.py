# Generated by Django 3.2.5 on 2024-11-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0047_workshop_endtime_workshop_starttime_workshop_title2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='contact',
        ),
        migrations.AlterField(
            model_name='workshop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Obrázek'),
        ),
    ]
