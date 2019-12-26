from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', None)


@login_required
def logout(request):
    django_logout(request)
    return render(request, 'index.html', None)
