from django.core.mail import send_mail
from birras.settings import EMAIL_FROM
from jinja2 import Template
from django.http import HttpRequest
from birras import settings


template_weekly_email = '''
 Meetups Of the week
 
 {% for meetup in list_meetup %}
     {{ meetup }}
 {% endfor %}
 
 See You!!
'''

template_confirm_registration = '''
Please activate account

Click the following address

{{endpoint}}

the meetups birras team

'''

template_confirm_delete_registration = '''
Please to delete your account

Click the following address

{{endpoint}}

the meetups birras team

'''
def fake_send_mail(subject, message, email_from, list_to, fail_silently):
    print(f'SUBJECT {subject}')
    print(f'MESSAGE {message}')
    print(f'email FROM   {email_from}')
    print(f'email TO      {list_to}')
    print(f'fail_silently {fail_silently}')

def send_meetup_notifications(email, list_meetup):
    '''
    Send an email notification of the week to meeters
    :param email:
    :param list_meetup:
    :return:
    '''

    template = Template(template_weekly_email)
    message = template.render(list_meetup=list_meetup)

    # TODO email service
    fake_send_mail(
        'Meet Ups Of the Week',
        message,
        EMAIL_FROM,
        [email],
        fail_silently=False,
    )


def send_register_confirmation_email(email):
    '''
    send register confirmation email
    :param email:
    :return:
    '''

    host = settings.SERVER_HOST

    url = f'{host}/confirm_create_meeter/{email}/'
    # TODO email service for register confirmation

    template = Template(template_confirm_registration)
    message = template.render(endpoint=url)

    fake_send_mail(
        'Confirm your registration',
        message,
        EMAIL_FROM,
        [email],
        fail_silently=False,
    )

    return {'error': False}


def send_register_delete_confirmatiom(email):
    '''
    send register confirmation email
    :param email:
    :return:
    '''

    host = settings.SERVER_HOST

    url = f'{host}/confirm_delete_meeter/{email}/'
    # TODO email service for register confirmation

    template = Template(template_confirm_delete_registration)
    message = template.render(endpoint=url)

    fake_send_mail(
        'Confirm delete registration',
        message,
        EMAIL_FROM,
        [email],
        fail_silently=False,
    )

    return {'error': False}
