from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from account.models import Team

from .constants import TicketPriority, TicketStatus
from .exceptions import NotEnoughInfoException


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
    assigned_to = GenericForeignKey('assignee_type', 'assignee_id')
    assignee_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, null=True, blank=True)
    assignee_id = models.PositiveIntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=30,
        choices=[(status.name, status.value) for status in TicketStatus],
        default=TicketStatus.NEW.value
    )
    # attachments = ???

    def update_status(self, status):
        assert status in TicketStatus, 'Unable to update status to %s'
        self.status = status.value
        self.save()

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)

        from review.models import Conversation
        Conversation.objects.get_or_create(ticket=self)


class Assignee(models.Model):
    pass


class AssignedUser(Assignee):
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class AssignedAnonymousUser(Assignee):
    # TODO: if someone joins the system we'll want to turn all of their
    # AssignedAnonymousUser entries into AssignedUser entries
    email = models.CharField(max_length=100, null=True, blank=True)
    slack_id = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        if self.email:
            return str('%s (Email)' % self.email)
        if self.slack_id:
            return str('%s (Slack)' % self.slack_id)

    def save(self, *args, **kwargs):
        if not self.email and not self.slack_id:
            raise NotEnoughInfoException(
                'Either email or Slack ID must be provided'
            )
        
        super(AssignedAnonymousUser, self).save(*args, **kwargs)


class AssignedTeam(Assignee):
    team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True)


class LinkedUser(Assignee):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    slack_id = models.CharField(max_length=100, null=True, unique=True)
    # TODO: a user can only have one email? Maybe not
    email = models.CharField(max_length=100, null=True, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
