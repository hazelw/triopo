from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='log-ticket'),
    re_path(
        'ticket/(?P<ticket_id>[0-9]+)/change-assignment/$',
        views.change_assignment,
        name='change-assignment'
    ),
    re_path(
        'ticket/(?P<ticket_id>[0-9]+)/change-ticket-status/$',
        views.change_ticket_status,
        name='change-ticket-status'
    ),
]
