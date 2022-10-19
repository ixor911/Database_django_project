from django.core import serializers
from django.shortcuts import render, redirect
from django.core.management import call_command
from .models import *
from django.core.management.commands import loaddata
import tempfile


def index(request):
    if request.method == 'POST':
        call_command('flush', '--no-input')
        call_command('migrate')
        return redirect('loadDatabase')

    return render(request, 'main/index.html')


def loadDatabase(request):
    if request.method == 'POST':
        call_command('loaddata', 'D:/all_for_prog/db.json', app_label='main')

        if 'file' in request.FILES:
            file = request.FILES.get('file')
            print(file)

    return render(request, 'main/loadDatabase.html')


def createDatabase(request):
    return render(request, 'main/createDatabase.html')


def getTables(request):
    context = {
        'tables': Table.objects.order_by('id')
    }

    return render(request, 'main/getTables.html', context)
