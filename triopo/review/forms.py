from django import forms

from ticketing.constants import TicketStatus


class ReplyForm(forms.Form):
    text = forms.CharField(max_length=1000)
    status = forms.ChoiceField(
        choices=[(status.name, status.value) for status in TicketStatus]
    )
