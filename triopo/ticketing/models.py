from django.contrib.auth.models import User
from django.db import models

from ticketing.constants import TicketStatus


class Ticket(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000)
    regarding_user_id = models.CharField(max_length=8, null=True, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.PROTECT)
    # TODO: what if the User doesn't have an account on the system? What
    # if we want to assign to a team instead?
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    status = models.CharField(choices=TicketStatus)
    # attachments = ???
