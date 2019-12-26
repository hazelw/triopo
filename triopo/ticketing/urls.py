from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='log-ticket'),
    re_path(
        'ticket/(?P<ticket_id>[0-9]+)/change-assignment/$',
        views.change_assignment,
        name='change-assignment'
    )
]
