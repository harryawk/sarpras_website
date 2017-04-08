from django.shortcuts import render
from .models import Log


# Log index view
def index(request):
    all_log = Log.objects.all()
    return render(request, 'log/index.html', {
        'all_log': all_log
    })