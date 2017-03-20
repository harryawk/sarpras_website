from django.shortcuts import render
from django.http import HttpResponse
from .models import Peminjam


# Peminjam index view, mostly for debugging purpose
def index(request):
    all_peminjam = Peminjam.objects.all()
    return render(request, 'peminjam/index.html', {
        'all_peminjam': all_peminjam
    })


# Return a form which'll be used to add new Peminjam object to model
def formadd(request):
    return render(request, 'peminjam/add.html', {})

# Will be called by addForm, will process the new peminjam data
def processadd(request):
    return HttpResponse("",status=200)


# Return a form which'll be used to edit Peminjam object to model
def formedit(request, peminjam_id):
    return render(request, 'peminjam/edit.html', {})

# Will be called by addForm, will process the edited peminjam data
def processedit(request, peminjam_id):
    return HttpResponse("",status=200)


# Return a form which'll be used to delete Peminjam object to model
def formdelete(request, peminjam_id):
    return render(request, 'peminjam/delete.html', {})

# Will be called by addForm, will process the deleted peminjam data
def processdelete(request, peminjam_id):
    return HttpResponse("",status=200)

