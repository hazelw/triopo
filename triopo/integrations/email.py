from django.template.loader import render_to_string
import requests
import os


MAILGUN_API_DOMAIN = os.getenv('MAILGUN_API_DOMAIN')
MAILGUN_ENDPOINT = f'https://api.mailgun.net/v3/{MAILGUN_API_DOMAIN}/messages'


def new_assignment_email(email_address, ticket):
    send_email(
        to_address=email_address,
        subject='New ticket assigned to you',
        html=render_to_string('new_assignment.html')
    )


def send_email(
    from_details='Triopo <triopo@hazelsarahwright.com>',
    to_address=None, subject='', text=''
):
    api_key = os.getenv('MAILGUN_API_KEY', None)
    requests.post(
        MAILGUN_ENDPOINT,
        auth=('api', api_key),
        data={
            'from': from_details,
            'to': to_address,
            'subject': subject,
            'text': text
        }
    )
