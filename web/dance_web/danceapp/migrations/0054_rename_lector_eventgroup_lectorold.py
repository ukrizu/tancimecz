# Generated by Django 3.2.5 on 2025-01-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0053_auto_20250116_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventgroup',
            old_name='lector',
            new_name='lectorOld',
        ),
    ]
