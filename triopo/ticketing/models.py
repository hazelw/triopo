from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from account.models import Team
from ticketing.constants import TicketPriority, TicketStatus


class Ticket(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000)
    regarding_user_id = models.CharField(max_length=8, null=True, blank=True)
    priority = models.CharField(
        max_length=30,
        choices=[(priority.name, priority.value) for priority in TicketPriority],
        default=TicketPriority.MEDIUM.value
    )
    submitted_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True,
        related_name='submitted_ticket'
    )
    assignee_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, null=True, blank=True)
    assignee_id = models.PositiveIntegerField(null=True, blank=True)
    assigned_to = GenericForeignKey('assignee_type', 'assignee_id')

    status = models.CharField(
        max_length=30,
        choices=[(status.name, status.value) for status in TicketStatus],
        default=TicketStatus.NEW.value
    )
    # attachments = ???


class Assignee(models.Model):
    pass


class AssignedUser(Assignee):
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class AssignedAnonymousUser(Assignee):
    # TODO: if someone joins the system we'll want to turn all of their
    # AssignedAnonymousUser entries into AssignedUser entries
    email = models.CharField(max_length=100, null=True, blank=True)
    slack_id = models.CharField(max_length=60, null=True, blank=True)

    def __init__(*args, **kwargs):
        if email not in kwargs:
            assert kwargs.get('slack_id') is not None

        if slack_id not in kwargs:
            assert kwargs.get('email') is not None


class AssignedTeam(Assignee):
    team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True)
