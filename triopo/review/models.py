from django.contrib.auth.models import User
from django.db import models

from ticketing.models import Ticket


class Conversation(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)


class Reply(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    text = models.CharField(max_length=1000)
    submitted_by = models.ForeignKey(User, on_delete=models.PROTECT)
