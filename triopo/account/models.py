from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    email = models.CharField(max_length=100)
    slack_name = models.CharField(max_length=100)


class SlackIdentity(models.Model):
    name = models.CharField(max_length=100)
    slack_id = models.CharField(max_length=12)
