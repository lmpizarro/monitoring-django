# Generated by Django 3.1 on 2020-08-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_checkinmeetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='checkin',
            field=models.ManyToManyField(related_name='meeters_checkin', to='app.Meeter'),
        ),
    ]
