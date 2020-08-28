# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import task
from app.management.commands.updatetemperature import updatetemperature

@shared_task
def add(x, y):
    return x + y
    
 

# We can have either registered task 
@task(name='newtemperature')
def newtemperature():
    updatetemperature()
    return 'NEW TEMPERATURE'
 
@shared_task 
def send_notification():
     print('Here I am')
     return "NOTIFICATION"
