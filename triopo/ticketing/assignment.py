from .models import Ticket


def clear_ticket_assignment(ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = None
    ticket.save()


def assign_ticket_to_team(ticket_id, team):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = team
    ticket.save()


def assign_ticket_to_user(ticket_id, user):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = user
    ticket.save()


def assign_ticket_to_email(ticket_id, email):
    pass


def assign_ticket_to_slack_id(ticket_id, slack_id):
    pass
