from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render

from ticketing.models import Ticket
from ticketing.constants import TicketStatus

from .controller import create_reply
from .forms import ReplyForm


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

    form = ReplyForm(ticket=ticket)

    context = {
        'ticket': ticket,
        'form': form
    }

    return render(request, 'ticket.html', context)


@login_required(login_url='/login/')
def reply(request, ticket_id):
    if not request.POST:
        raise Http404

    text = request.POST.get('text')
    status = request.POST.get('status')

    create_reply(ticket_id, request.user, text, status)

    return view_ticket(request, ticket_id)
