from django import forms

from ticketing.constants import TicketStatus


class ReplyForm(forms.Form):
    text = forms.CharField(max_length=1000)
    status = forms.ChoiceField(
        choices=[(status.value, status.value) for status in TicketStatus]
    )

    def __init__(self, *args, **kwargs):
        if 'ticket' in kwargs:
            initial_status = kwargs['ticket'].status
            kwargs.pop('ticket')
        else:
            initial_status = None

        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = initial_status
