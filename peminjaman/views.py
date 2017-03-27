from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pembayaran, Peminjaman
from ruangan.models import Ruangan
from peminjam.models import Peminjam
from datetime import datetime

# Peminjaman index view, mostly for debugging purpose
def index(request, errormsg=''):
    all_peminjaman = Peminjaman.objects.all()
    return render(request, 'peminjaman/index.html', {
        'all_peminjaman' : all_peminjaman,
        'error' : errormsg
    })


# Return a form which'll be used to add new Peminjaman object to model
def formadd(request):

    if request.method == 'POST':
        # Ambil data hasil input dari user
        input_peminjam = request.POST['peminjam']
        input_ruangan = request.POST['ruangan']

        tanggal_mulai_pinjam = request.POST['waktu_awal_0'] # format tanggal : %Y-%m-%d
        tanggal_mulai_pinjam = datetime.strptime(tanggal_mulai_pinjam, "%Y-%m-%d")
        print("tanggal_mulai_pinjam : ", tanggal_mulai_pinjam)
        pukul_mulai_pinjam = request.POST['waktu_awal_1'] # format waktu : %H:%M
        x = datetime.strptime(pukul_mulai_pinjam, "%H:%M")
        # print datetime.time()
        tanggal_mulai_pinjam = tanggal_mulai_pinjam.replace(hour=x.hour, minute=x.minute)
        print("Setelah : " + str(tanggal_mulai_pinjam))
        print(x.hour, x.minute, x.second)
        tanggal_selesai_pinjam = request.POST['waktu_akhir_0']
        tanggal_selesai_pinjam = datetime.strptime(tanggal_selesai_pinjam, "%Y-%m-%d")
        pukul_selesai_pinjam = request.POST['waktu_akhir_1']
        y = datetime.strptime(pukul_selesai_pinjam, "%H:%M")
        tanggal_selesai_pinjam = tanggal_selesai_pinjam.replace(hour=y.hour, minute=y.minute)
        input_deskripsi = request.POST['deskripsi']

        obj_peminjam = Peminjam.objects.get(id=input_peminjam)
        obj_ruangan = Ruangan.objects.get(id=input_ruangan)
        try:
            Peminjaman.objects.get(peminjam=obj_peminjam, ruangan=obj_ruangan, waktu_awal=tanggal_mulai_pinjam, waktu_akhir=tanggal_selesai_pinjam)
        except Peminjaman.DoesNotExist:
            new_transaction = Peminjaman(peminjam=obj_peminjam,
                                         ruangan=obj_ruangan,
                                         waktu_awal=tanggal_mulai_pinjam,
                                         waktu_akhir=tanggal_selesai_pinjam,
                                         deskripsi=input_deskripsi)
            new_transaction.save()
    # Peminjam.objects.get(peminjam=input_peminjam)
    # Ruangan.objects.get(ruangan=input_ruangan)
    all_peminjam = Peminjam.objects.all()
    all_ruangan = Ruangan.objects.all()
    return render(request, 'peminjaman/add.html', {
        'all_peminjam' : all_peminjam,
        'all_ruangan' : all_ruangan,
    })


# Return a form which'll be used to edit peminjaman object to model
def formedit(request, peminjaman_id):
    return render(request, 'peminjaman/edit.html', {})


# Return a form which'll be used to delete peminjaman object to model
def formdelete(request, peminjaman_id, errormsg=''):
    try:
        object_peminjaman = Peminjaman.objects.get(id=peminjaman_id)
        object_peminjaman.delete()
    except Peminjaman.DoesNotExist:
        pass
    all_peminjaman = Peminjaman.objects.all()
    pass
    return render(request, 'peminjaman/index.html', {
        'all_peminjaman': all_peminjaman,
        'error': errormsg
    })
    # return render(request, 'peminjaman/delete.html', {})

