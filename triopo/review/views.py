from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render

from ticketing.models import Ticket
from ticketing.constants import TicketStatus


@login_required(login_url='/login/')
def index(request):
    # TODO: serious pagination, filtering by status and priority, assigned_to/
    # created_by - this is just one big yikes for now

    tickets = Ticket.objects.filter(status__in=[
        TicketStatus.NEW.value,
        TicketStatus.TRIAGED.value,
        TicketStatus.ON_HOLD.value
    ]).order_by('-updated_at')

    context = {
        'tickets': tickets
    }

    return render(request, 'review.html', context)


@login_required(login_url='/login/')
def view_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        raise Http404

    context = {
        'ticket': ticket
    }

    return render(request, 'ticket.html', context)
