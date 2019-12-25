from django.http import HttpResponse
from django.shortcuts import render

from ticketing.models import Ticket
from ticketing.constants import TicketStatus


def index(request):
    # TODO: serious pagination, filtering by status and priority
    # this is just one big yikes for now

    tickets = Ticket.objects.filter(status__in=[
        TicketStatus.NEW, TicketStatus.TRIAGED, TicketStatus.ON_HOLD    
    ]).order_by('-updated_date')

    return HttpResponse('Review tickets here')
