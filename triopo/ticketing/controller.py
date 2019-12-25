from .models import Ticket


def build_ticket(creator, title, description, regarding_user_id, priority):
    Ticket.objects.create(
        title=title,
        description=description,
        regarding_user_id=regarding_user_id,
        priority=priority,
        submitted_by=creator
    )
