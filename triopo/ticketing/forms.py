from django import forms
from django.contrib.auth.models import User

from account.models import Team

from .constants import TicketPriority


class TicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    regarding_user_id = forms.CharField(max_length=8)
    priority = forms.ChoiceField(
        choices=[(priority.name, priority.value) for priority in TicketPriority]
    )


class ChangeAssignmentForm(forms.Form):
    team = forms.ModelChoiceField(
        queryset=Team.objects.filter(is_active=True),
        empty_label='N/A',
        required=False
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        empty_label='N/A',
        required=False
    )
    email = forms.CharField(max_length=150, required=False)
    slack_id = forms.CharField(max_length=150, required=False)
