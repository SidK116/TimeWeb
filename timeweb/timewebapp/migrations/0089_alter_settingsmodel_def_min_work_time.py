# Generated by Django 3.2.7 on 2021-11-19 09:08

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timewebapp', '0088_alter_timewebmodel_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmodel',
            name='def_min_work_time',
            field=models.DecimalField(blank=True, decimal_places=2, default=15, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), 'The default minimum work time must be positive')], verbose_name='Default Minimum Daily Work Time in Minutes'),
        ),
    ]
