# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import task
from app.management.commands.updatetemperature import updatetemperature
from app.services.notifications import Notifications
from app.services.emailsender import send_meetup_notifications
from app.services.emailsender import send_meetup_delete_notification



@task(name='newtemperature')
def newtemperature():
    updatetemperature()
    return 'NEW TEMPERATURE'


@shared_task
def send_notification_delete_meetup(email, name):
    send_meetup_delete_notification(email, name)
    return f"NOTIFICATION {email} DELETE MEETUP {name}"


@shared_task
def send_emails_week_meetups(email_tuple):

    email = email_tuple[0]
    meetup_list = email_tuple[1]

    # Send an email notification of the meetups of the week to meeters
    send_meetup_notifications(email, meetup_list)

    return f'NOTIFICATION WEEK MEETUP {email}'


@task(name='week_meetups')
def week_meetups():
    notifications = Notifications()

    emails_to_notify = notifications.week_meetups()

    for email in emails_to_notify[0]:
        send_emails_week_meetups.delay(email, emails_to_notify[1])

    return 'WEEK_MEETUPS'

