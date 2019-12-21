# Generated by Django 3.0.1 on 2019-12-21 21:19

from django.conf import settings
from django.db import migrations, models
import ticketing.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('regarding_user_id', models.CharField(blank=True, max_length=8, null=True)),
                ('priority', models.CharField(choices=[(ticketing.constants.TicketPriority['LOW'], 'low'), (ticketing.constants.TicketPriority['MEDIUM'], 'medium'), (ticketing.constants.TicketPriority['HIGH'], 'high')], max_length=30)),
                ('status', models.CharField(choices=[(ticketing.constants.TicketStatus['NEW'], 'new'), (ticketing.constants.TicketStatus['TRIAGED'], 'triaged'), (ticketing.constants.TicketStatus['ON_HOLD'], 'on hold'), (ticketing.constants.TicketStatus['DONE'], 'done')], max_length=30)),
                ('assigned_to', models.ManyToManyField(related_name='assigned_ticket', to=settings.AUTH_USER_MODEL)),
                ('submitted_by', models.ManyToManyField(related_name='submitted_ticket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]