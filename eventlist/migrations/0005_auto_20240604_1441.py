# Generated by Django 3.2.5 on 2024-06-04 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlist', '0004_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='DateTime'),
        ),
    ]
