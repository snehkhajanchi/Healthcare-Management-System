# Generated by Django 3.0.5 on 2020-04-28 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20200428_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='health_service_income',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor',
            field=models.ForeignKey(limit_choices_to={'groups': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='nurse',
            field=models.ForeignKey(limit_choices_to={'groups': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='Nurse', to=settings.AUTH_USER_MODEL),
        ),
    ]
