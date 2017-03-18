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


# Return a form which'll be used to edit peminjaman object to model
def formedit(request, peminjaman_id):
    return render(request, 'peminjaman/edit.html', {})

# Will be called by addForm, will process the edited peminjaman data
def processedit(request, peminjaman_id):
    return HttpResponse("",status=200)


# Return a form which'll be used to delete peminjaman object to model
def formdelete(request, peminjaman_id):
    return render(request, 'peminjaman/delete.html', {})

# Will be called by addForm, will process the deleted peminjaman data
def processdelete(request, peminjaman_id):
    return HttpResponse("",status=200)