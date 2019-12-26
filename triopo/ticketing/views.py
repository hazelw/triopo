from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .controller import build_ticket
from .assignment import (
    clear_ticket_assignment,
    assign_ticket_to_team,
    assign_ticket_to_user,
    assign_ticket_to_email,
    assign_ticket_to_slack_id
)

from .constants import TicketStatus
from .forms import TicketForm, ChangeAssignmentForm
from .models import Ticket


@login_required(login_url='/login/')
def index(request):
    form = TicketForm()
    context = {'form': form}

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = build_ticket(
                request.user,
                form.cleaned_data.get('title'),
                form.cleaned_data.get('description'),
                form.cleaned_data.get('regarding_user_id'),
                form.cleaned_data.get('priority')
            )
            return redirect(reverse('view-ticket', args=[ticket.id]))

    return render(request, 'log_ticket.html', context)


@login_required(login_url='/login/')
def change_assignment(request, ticket_id):
    form = ChangeAssignmentForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ChangeAssignmentForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            slack_id = form.cleaned_data['slack_id']

            field_values = [
                field for field in [team, user, email, slack_id] if field
            ]
            print(field_values)

            if len(field_values) > 1:
                # TODO: avoid raw exception
                raise Exception(
                    'You should only provide the user, email address OR slack ID'
                )

            if len(field_values) == 0:
                clear_ticket_assignment(ticket_id)
            elif team:
                assign_ticket_to_team(ticket_id, team)
            elif user:
                assign_ticket_to_user(ticket_id, user)
            elif email:
                assign_ticket_to_email(ticket_id, email)
            elif slack_id:
                assign_ticket_to_slack_id(ticket_id, slack_id)

            return redirect(reverse('view-ticket', args=[ticket_id]))

    return render(request, 'change_assignment.html', context)
