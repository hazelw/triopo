from django import forms

from .constants import TicketPriority


class TicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    regarding_user_id = forms.CharField(max_length=8)
    priority = forms.ChoiceField(
        choices=[(priority.name, priority.value) for priority in TicketPriority]
    )
