# Generated by Django 3.0.5 on 2020-04-11 17:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200411_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 17, 4, 53, 996587, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 17, 4, 53, 996561, tzinfo=utc)),
        ),
    ]
