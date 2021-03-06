# Generated by Django 3.1 on 2020-08-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('meet_date', models.DateTimeField(null=True, verbose_name='meet up date')),
                ('place', models.TextField(max_length=512, null=True, verbose_name='The Place')),
                ('description', models.TextField(max_length=512, null=True, verbose_name='Brief')),
            ],
        ),
        migrations.CreateModel(
            name='Meeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Meeter Name')),
                ('meetups', models.ManyToManyField(to='app.MeetUP')),
            ],
        ),
    ]
