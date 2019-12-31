from django.db.models import Q

from .exceptions import ContradictoryUserDetailsException
from .models import Ticket, LinkedUser, AssignedUser, AssignedAnonymousUser


def build_ticket(creator, title, description, regarding_user_id, priority):
    return Ticket.objects.create(
        title=title,
        description=description,
        regarding_user_id=regarding_user_id,
        priority=priority,
        submitted_by=creator
    )


def get_all_assigned_tickets_for_user(user=None, slack_id=None, email=None):
    # TODO: this smells a bit like the assignee data model isn't right
    assert user or slack_id or email, \
        'You must define which user you are looking for'

    tickets = []

    # First - check if we have a LinkedUser for this person
    try:
        linked_user = LinkedUser.objects.get(
            Q(user=user) | Q(slack_id=slack_id) | Q(email=email)
        )

        tickets = Ticket.objects.filter(assigned_to=linked_user)
    except LinkedUser.DoesNotExist:
        # TODO: there must be a better way of doing this
        contact_types = [user, slack_id, email]
        if len([
            contact_type for contact_type in contact_types
            if contact_type is not None
        ]) > 1:
            raise ContradictoryUserDetailsException()

        if user:
            assignments = AssignedUser.objects.filter(user=user)
        elif slack_id:
            assignments = AssignedAnonymousUser.objects.filter(slack_id=slack_id)
        elif email:
            assignments = AssignedAnonymousUser.objects.filter(email=email)
        
        tickets = Ticket.objects.filter(assigned_to__in=assignments)

    return tickets


def get_all_assigned_tickets_for_team(team):
    pass
