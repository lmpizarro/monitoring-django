# Generated by Django 3.1 on 2020-08-27 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200827_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttemperature',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='time'),
        ),
    ]
