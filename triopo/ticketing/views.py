from django.http import HttpResponse
from django.shortcuts import render

from .constants import TicketStatus
from .models import Ticket


def index(request):
    # TODO: serious pagination, filtering by status and priority
    # this is just one big yikes for now

    tickets = Ticket.objects.filter(status__in=[
        TicketStatus.NEW, TicketStatus.TRIAGED, TicketStatus.ON_HOLD    
    ]).order_by('-updated_date')

    return HttpResponse('display tickets here')


def create_ticket(request):
    pass


def delete_ticket(request):
    pass
