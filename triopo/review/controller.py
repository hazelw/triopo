from datetime import datetime

from .models import Conversation, Reply


def create_reply(ticket_id, user, text, status):
    # TODO: if the status has changed we should be creating some kind of status
    # change audit trail too

    convo = Conversation.objects.get(ticket_id=ticket_id)
    now = datetime.now()

    reply = Reply.objects.create(
        conversation=convo,
        created_at=now,
        text=text,
        submitted_by=user
    )

    # TODO: has the status changed? update ticket status if so. we'll want
    # to make sure the status dropdown is set to the current status
    # of the ticket by default
