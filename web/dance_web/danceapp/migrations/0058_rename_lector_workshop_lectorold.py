# Generated by Django 3.2.5 on 2025-01-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0057_auto_20250116_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='lector',
            new_name='lectorOld',
        ),
    ]
