from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='view-tickets'),
    re_path('ticket/(?P<ticket_id>[0-9]+)/$', views.view_ticket, name='view-ticket'),
    re_path('ticket/(?P<ticket_id>[0-9]+)/reply', views.reply, name='reply'),
]
