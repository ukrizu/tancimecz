# Generated by Django 3.2.5 on 2024-07-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0023_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='coordinates',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]