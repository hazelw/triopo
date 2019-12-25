from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from ticketing.controller import build_ticket

from .constants import TicketStatus
from .forms import TicketForm
from .models import Ticket


@login_required(login_url='/login/')
def index(request):
    form = TicketForm()
    context = {'form': form}

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            build_ticket(
                request.user,
                form.cleaned_data.get('title'),
                form.cleaned_data.get('description'),
                form.cleaned_data.get('regarding_user_id'),
                form.cleaned_data.get('priority')
            )
            messages.success(request, 'Ticket successfully submitted')

    return render(request, 'log_ticket.html', context)
