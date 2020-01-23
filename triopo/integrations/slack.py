import os
from slack import WebClient

from account.models import SlackIdentity
from .exceptions import SlackIdNotFoundException


def _refresh_slack_identities():
    token = os.getenv('SLACK_API_TOKEN')
    client = WebClient(token)

    response = client.users_list()
    for member in response['members']:
        SlackIdentity.objects.get_or_create(
            name=member['name'], slack_id=member['slack_id']
        )
    

def send_notification_to_slack_user(user):
    try:
        slack_identity = SlackIdentity.objects.get(name=user)
    except SlackIdentity.DoesNotExist:
        _refresh_slack_identities()
        
        if not SlackIdentity.objects.exists(name=user):
            raise SlackIdNotFoundException()

    token = os.getenv('SLACK_API_TOKEN')
    client = WebClient(token)

    # ??? might be a different channel name
    client.chat_postMessage(
        channel=slack_identity.slack_id,
        text='You have been assigned a new ticket on Triopo'
    )
