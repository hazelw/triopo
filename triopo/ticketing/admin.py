from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'regarding_user_id', 'priority', 'status'
    )
    # TODO: sort out assigned_to, reported_by


admin.site.register(Ticket, TicketAdmin)
