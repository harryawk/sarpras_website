from django.shortcuts import render
from django.http import HttpResponse


# Peminjam index view, mostly for debugging purpose
def index(request):
    return render(request, 'peminjam/index.html', {})


# Return a form which'll be used to add new Peminjam object to model
def formadd(request):
    return render(request, 'peminjam/add.html', {})


# Will be called by addForm, will process the new peminjam data
def processadd(request):
    return HttpResponse("",status=200)