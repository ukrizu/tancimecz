# Generated by Django 3.2.5 on 2024-11-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0051_auto_20241116_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='title1',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title2',
            field=models.CharField(blank=True, max_length=101, null=True, verbose_name='Název - 2. řádek (nepovinné)'),
        ),
    ]
