# Generated by Django 3.2.5 on 2024-12-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0051_alter_eventgroup_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date'], 'verbose_name': 'Taneční večer', 'verbose_name_plural': 'Taneční večery'},
        ),
        migrations.AlterModelOptions(
            name='eventgroup',
            options={'ordering': ['-startTime'], 'verbose_name': 'Taneční večer', 'verbose_name_plural': 'Taneční večery'},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['-start'], 'verbose_name': 'Workshop', 'verbose_name_plural': 'Workshopy'},
        ),
        migrations.AddField(
            model_name='lector',
            name='fb',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Facebook'),
        ),
    ]