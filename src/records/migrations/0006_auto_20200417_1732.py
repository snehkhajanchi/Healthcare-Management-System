# Generated by Django 3.0.5 on 2020-04-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20200417_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='height_inches',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')], default=0),
        ),
    ]
