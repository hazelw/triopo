# Generated by Django 3.0.1 on 2019-12-21 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='submitted_by',
        ),
    ]
