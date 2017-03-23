from django.shortcuts import render
from django.http import HttpResponse
from .models import Pembayaran, Peminjaman
from ruangan.models import Ruangan
from peminjam.models import Peminjam


# Peminjaman index view, mostly for debugging purpose
def index(request, errormsg):
    all_peminjaman = Peminjaman.objects.all()
    return render(request, 'peminjaman/index.html', {
        'all_peminjaman' : all_peminjaman,
        'error' : errormsg
    })


# Return a form which'll be used to add new Peminjaman object to model
def formadd(request):
    return render(request, 'peminjaman/add.html', {})


# Return a form which'll be used to edit peminjaman object to model
def formedit(request, peminjaman_id):
    return render(request, 'peminjaman/edit.html', {})


# Return a form which'll be used to delete peminjaman object to model
def formdelete(request, peminjaman_id):
    return render(request, 'peminjaman/delete.html', {})

