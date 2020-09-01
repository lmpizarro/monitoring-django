from django.core.mail import send_mail
from birras.settings import EMAIL_FROM
from jinja2 import Template
from django.http import HttpRequest

template_weekly_email = '''
 Meetups Of the week
 
 {% for meetup in list_meetup %}
     {{ meetup }}
 {% endfor %}
 
 See You!!
'''

template_confirm_registration = '''
Please send confirmation

Click the following address

{{endpoint}}

'''

def fake_send_mail(subject, message, email_from, list_to, fail_silently):
    print(subject)
    print(message)
    print(email_from)
    print(list_to)
    print(fail_silently)

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

    host = HttpRequest.get_host()

    url = f'{host}/confirm_registration/{email}/'
    # TODO email service for register confirmation

    template = Template(template_confirm_registration)
    message = template.render(endpoint=url)

    fake_send_mail(
        'Meet Ups Of the Week',
        message,
        EMAIL_FROM,
        [email],
        fail_silently=False,
    )
