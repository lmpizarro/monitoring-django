# Generated by Django 3.1 on 2020-08-27 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200827_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currenttemperature',
            old_name='temperature',
            new_name='temp',
        ),
        migrations.AlterField(
            model_name='currenttemperature',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='time'),
        ),
    ]
