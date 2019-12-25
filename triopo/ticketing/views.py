from django.http import HttpResponse
from django.shortcuts import render

from .constants import TicketStatus
from .forms import TicketForm
from .models import Ticket


def index(request):
    form = TicketForm()
    context = {'form': form}

    # TODO: check for post
    if form.is_valid():
        pass

    return render(request, 'log_ticket.html', context)


def create_ticket(request):
    pass


def delete_ticket(request):
    pass
