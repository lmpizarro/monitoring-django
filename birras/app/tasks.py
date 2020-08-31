# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import task
from app.management.commands.updatetemperature import updatetemperature

@task(name='newtemperature')
def newtemperature():
    updatetemperature()
    return 'NEW TEMPERATURE'
 
@shared_task
def send_notification_delete_meetup(email):
     return f"NOTIFICATION DELETE MEETUP {email}"
