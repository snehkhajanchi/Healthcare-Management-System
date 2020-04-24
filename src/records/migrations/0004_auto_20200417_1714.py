# Generated by Django 3.0.5 on 2020-04-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20200417_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='blood_pressure',
            field=models.CharField(blank=True, default='0/0', max_length=7),
        ),
        migrations.AlterField(
            model_name='record',
            name='height_feet',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='height_inches',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')], default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='pulse',
            field=models.PositiveIntegerField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='record',
            name='reason_for_visit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='weight_lbs',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]