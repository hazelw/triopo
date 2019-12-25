from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'regarding_user_id', 'priority',
                'submitted_by', 'assigned_to', 'status')
