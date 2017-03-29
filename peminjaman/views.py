from django.shortcuts import render, redirect
from django.urls import reverse
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

    input_peminjam = ''
    input_ruangan = ''

    tanggal_awal = request.POST.get('waktu_awal_0', '2016-01-31') # format tanggal : %Y-%m-%d
    tanggal_akhir = request.POST.get('waktu_akhir_0', '2017-01-31') # format tanggal : %Y-%m-%d

    pukul_awal = request.POST.get('waktu_awal_1', '00:00') # format waktu : %H:%M
    pukul_akhir = request.POST.get('waktu_akhir_1', '00:00') # format waktu : %H:%M

    input_deskripsi = request.POST.get('deskripsi', '')

    errormsg = []
    messages = []

    if request.method == 'POST':

        # Ambil data hasil input dari user
        input_peminjam = request.POST['peminjam']
        input_ruangan = request.POST['ruangan']

        # Ambil dan parsing tanggal-jam mulai pinjam dari form
        tanggal_mulai_pinjam = datetime.strptime(tanggal_awal, "%Y-%m-%d")
        mulai_pinjam = datetime.strptime(pukul_awal, "%H:%M")
        tanggal_mulai_pinjam = tanggal_mulai_pinjam.replace(hour=mulai_pinjam.hour, minute=mulai_pinjam.minute)

        # Ambil dan parsing tanggal-jam selesai pinjam dari form
        tanggal_selesai_pinjam = datetime.strptime(tanggal_akhir, "%Y-%m-%d")
        akhir_pinjam = datetime.strptime(pukul_akhir, "%H:%M")
        tanggal_selesai_pinjam = tanggal_selesai_pinjam.replace(hour=akhir_pinjam.hour, minute=akhir_pinjam.minute)

        # Ambil objek Peminjam dan Ruangan
        obj_peminjam = Peminjam.objects.get(id=input_peminjam)
        obj_ruangan = Ruangan.objects.get(id=input_ruangan)

        # Mengecek tanggal mulai kurang dari tanggal selesai
        temp_mulai = tanggal_mulai_pinjam.replace(tzinfo=None)
        temp_selesai = tanggal_selesai_pinjam.replace(tzinfo=None)
        if temp_mulai >= temp_selesai:
            errormsg += ['Waktu mulai harus kurang dari waktu selesai']

        # Jika belum ditemukan error
        if not errormsg:

            # Membuat object peminjaman yang sesuai, BELUM DI-SAVE
            new_peminjaman = Peminjaman(peminjam=obj_peminjam,
                                        ruangan=obj_ruangan,
                                        waktu_awal=tanggal_mulai_pinjam,
                                        waktu_akhir=tanggal_selesai_pinjam,
                                        deskripsi=input_deskripsi)

            # Mengecek apakah ada peminjaman yang bentrok,
            collision = new_peminjaman.get_all_conflicted_set()

            # Apabila tidak ada bentrok, maka simpan peminjaman, dan kembali ke index
            if(not collision):
                try:
                    new_peminjaman.save()
                except Exception as e:
                    messages += ["Unhandled Exception", ]
                else:
                    return redirect(reverse('peminjaman:index'))

            # Jika ada, print semua jadwal yang bentrok, dan kembalikan form
            else:
                errormsg += ['Terdapat jadwal yang bentrok :' ]
                for peminjaman in collision:
                    errormsg += [peminjaman.__str__(), ]

    # Apabila tidak redirect ke index, maka kirim form
    all_peminjam = Peminjam.objects.all()
    all_ruangan = Ruangan.objects.all()
    return render(request, 'peminjaman/add.html', {
        'all_peminjam': all_peminjam,
        'all_ruangan': all_ruangan,
        'error': errormsg,
        'message': messages,
        'input_peminjam': input_peminjam,
        'input_ruangan': input_ruangan,
        'input_deskripsi': input_deskripsi,
        'tanggal_awal': tanggal_awal,
        'pukul_awal': pukul_awal,
        'tanggal_akhir': tanggal_akhir,
        'pukul_akhir': pukul_akhir,
    })


# Return a form which'll be used to edit peminjaman object to model
def formedit(request, peminjaman_id):

    object_peminjaman = Peminjaman.objects.get(id=peminjaman_id)
    if request.method == 'POST':
        # Ambil data hasil input dari user
        input_peminjam = request.POST['peminjam']
        input_ruangan = request.POST['ruangan']

        tanggal_mulai_pinjam = request.POST['waktu_awal_0']  # format tanggal : %Y-%m-%d
        tanggal_mulai_pinjam = datetime.strptime(tanggal_mulai_pinjam, "%Y-%m-%d")
        pukul_mulai_pinjam = request.POST['waktu_awal_1']  # format waktu : %H:%M
        x = datetime.strptime(pukul_mulai_pinjam, "%H:%M")
        # print datetime.time()
        tanggal_mulai_pinjam = tanggal_mulai_pinjam.replace(hour=x.hour, minute=x.minute)

        tanggal_selesai_pinjam = request.POST['waktu_akhir_0']
        tanggal_selesai_pinjam = datetime.strptime(tanggal_selesai_pinjam, "%Y-%m-%d")
        pukul_selesai_pinjam = request.POST['waktu_akhir_1']
        y = datetime.strptime(pukul_selesai_pinjam, "%H:%M")
        tanggal_selesai_pinjam = tanggal_selesai_pinjam.replace(hour=y.hour, minute=y.minute)
        input_deskripsi = request.POST['deskripsi']

        obj_peminjam = Peminjam.objects.get(id=input_peminjam)
        obj_ruangan = Ruangan.objects.get(id=input_ruangan)
        errormsg = ''
        try:
            Peminjaman.objects.get(peminjam=obj_peminjam, ruangan=obj_ruangan, waktu_awal=tanggal_mulai_pinjam,
                                   waktu_akhir=tanggal_selesai_pinjam)
        except Peminjaman.DoesNotExist:
            object_peminjaman.peminjam=obj_peminjam
            object_peminjaman.ruangan=obj_ruangan
            object_peminjaman.waktu_awal=tanggal_mulai_pinjam
            object_peminjaman.waktu_akhir=tanggal_selesai_pinjam
            object_peminjaman.deskripsi=input_deskripsi
            object_peminjaman.save()
            return redirect(reverse('peminjaman:index'))

    all_peminjam = Peminjam.objects.all()
    all_ruangan = Ruangan.objects.all()
    return render(request, 'peminjaman/edit.html', {
        'all_peminjam': all_peminjam,
        'all_ruangan': all_ruangan,
        'object_peminjaman': object_peminjaman,
        'id_peminjaman': peminjaman_id,
    })


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
        'error': errormsg,
    })
    # return render(request, 'peminjaman/delete.html', {})
