# Generated by Django 3.2.5 on 2024-06-17 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0011_alter_event_lector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='danceapp.lector'),
        ),
    ]
