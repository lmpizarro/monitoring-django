# Generated by Django 3.1 on 2020-09-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_checkinmeetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeter',
            name='create_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]
