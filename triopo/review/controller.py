from datetime import datetime

from django.db import transaction
from django.http import Http404

from ticketing.models import Ticket

from .models import Conversation, Reply


@transaction.atomic()
def create_reply(ticket_id, user, text, status):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except:
        return Http404

    # has the ticket status changed? TODO: reconcile this with the function on
    # Ticket, add audit trail
    if ticket.status != status:
        ticket.status = status
        ticket.save()

    convo = Conversation.objects.get(ticket_id=ticket_id)
    now = datetime.now()

    reply = Reply.objects.create(
        conversation=convo,
        created_at=now,
        text=text,
        submitted_by=user
    )
