# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import task
from app.management.commands.updatetemperature import updatetemperature

@task(name='newtemperature')
def newtemperature():
    updatetemperature()
    return 'NEW TEMPERATURE'
 
@task(name='send_notification')
def send_notification():
     print('Here I am')
     return "NOTIFICATION"
