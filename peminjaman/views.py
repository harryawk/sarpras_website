from django.shortcuts import render
from django.http import HttpResponse


# Peminjaman index view, mostly for debugging purpose
def index(request):
    return render(request, 'peminjaman/index.html', {})


# Return a form which'll be used to add new Peminjaman object to model
def formadd(request):
    return render(request, 'peminjaman/add.html', {})


# Will be called by addForm, will process the new peminjaman data
def processadd(request):
    return HttpResponse("", status=200)