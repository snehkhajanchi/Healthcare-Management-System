# Generated by Django 3.0.5 on 2020-04-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20200422_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_number',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_billed',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_owed',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
