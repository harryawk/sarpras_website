from django.shortcuts import render
from django.http import HttpResponse


# Ruangan index view, mostly for debugging purpose
def index(request):
    return render(request, 'ruangan/index.html', {})


# Return a form which'll be used to add new Ruangan object to model
def formadd(request):
    return render(request, 'ruangan/add.html', {})


# Will be called by addForm, will process the new ruangan data
def processadd(request):
    return HttpResponse("", status=200)