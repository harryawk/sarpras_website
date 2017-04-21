from django.shortcuts import render
from django.http import JsonResponse
from .models import Log
from django.contrib.auth.decorators import login_required

# Log index view
@login_required
def index(request):
    all_log = Log.objects.all();
    return render(request, 'log/index.html', {
        'all_log': all_log,
    })

@login_required
def fetchrecord(request, start_year = 2017):
    selected_log = Log.objects.filter(tanggal__year = start_year).values()
    return JsonResponse({'results': list(selected_log)})