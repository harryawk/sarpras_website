from django.shortcuts import render
from django.http import HttpResponse
from .models import Ruangan


# Ruangan index view, mostly for debugging purpose
def index(request):
    all_ruangan = Ruangan.objects.all()
    return render(request, 'ruangan/index.html', {
        'all_ruangan': all_ruangan
    })


# Return a form which'll be used to add new Ruangan object to model
def formadd(request):
    return render(request, 'ruangan/add.html', {})


# Return a form which'll be used to edit Ruangan object to model
def formedit(request, ruangan_id):
    return render(request, 'ruangan/edit.html', {})


# Return a form which'll be used to delete Ruangan object to model
def formdelete(request, ruangan_id):
    return render(request, 'ruangan/delete.html', {})

