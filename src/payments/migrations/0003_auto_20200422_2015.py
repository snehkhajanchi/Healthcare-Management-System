# Generated by Django 3.0.5 on 2020-04-22 20:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_invoice_date_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_billed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]