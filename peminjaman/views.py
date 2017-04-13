from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Peminjaman
from ruangan.models import Ruangan
from peminjam.models import Peminjam
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Peminjaman index view, mostly for debugging purpose
@login_required
def index(request, errormsg=''):
    all_peminjaman = Peminjaman.objects.all()
    all_ruangan = Ruangan.objects.all()
    all_peminjam = Peminjam.objects.all()
    return render(request, 'peminjaman/index.html', {
        'all_peminjaman' : all_peminjaman,
        'all_ruangan' : all_ruangan,
        'all_peminjam' : all_peminjam,
        'error' : errormsg
    })


@login_required
def kalender(request, errormsg=''):
    return render(request, 'peminjaman/kalender_admin.html', {})


# Return a form which'll be used to add new Peminjaman object to model
@login_required
def formadd(request):

    input_peminjam = ''
    input_ruangan = ''
    tanggal_awal = request.POST.get('waktu_awal_0', datetime.now().strftime("%Y-%m-%d")) # format tanggal : %Y-%m-%d
    tanggal_akhir = request.POST.get('waktu_akhir_0', datetime.now().strftime("%Y-%m-%d")) # format tanggal : %Y-%m-%d
    pukul_awal = request.POST.get('waktu_awal_1', '00:00') # format waktu : %H:%M
    pukul_akhir = request.POST.get('waktu_akhir_1', '00:00') # format waktu : %H:%M
    input_deskripsi = request.POST.get('deskripsi', '')
    input_tagihan = request.POST.get('harga', 0.00)
    input_tagihan = float(input_tagihan)
    input_nomor_surat = request.POST.get('nomor_surat', '')
    input_diskon = request.POST.get('discount', 0) # only for minus of input_tagihan

    errormsg = []
    messages = []

    if request.method == 'POST':

        # Ambil input tagihan dan Olah tagihan setelah dikurangi diskon
        input_tagihan = request.POST['harga']
        input_diskon = request.POST['discount']

        input_tagihan = float(input_tagihan)
        decimal_diskon = float(input_diskon) / float(100)
        input_tagihan = (1-decimal_diskon) * input_tagihan
        if input_tagihan < 0:
            input_tagihan = 0

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
            new_peminjaman = Peminjaman(no_laporan=input_nomor_surat,
                                        peminjam=obj_peminjam,
                                        ruangan=obj_ruangan,
                                        jumlah_tagihan=input_tagihan,
                                        waktu_awal=tanggal_mulai_pinjam,
                                        waktu_akhir=tanggal_selesai_pinjam,
                                        deskripsi=input_deskripsi)

            # Mengecek apakah ada peminjaman yang bentrok,
            collision = new_peminjaman.get_all_conflicted_set()

            # Apabila ada bentrok, print semua jadwal yang bentrok, dan kembalikan form
            if(collision):
                errormsg += ['Terdapat jadwal yang bentrok :']
                for peminjaman in collision:
                    errormsg += [peminjaman.__str__(), ]

            # Jika tidak, maka simpan peminjaman, dan kembali ke index
            else:
                try:
                    if int(input_diskon) > 0:
                        input_deskripsi = input_deskripsi + '\nDiskon : ' + input_diskon + ' %'
                        new_peminjaman.deskripsi = input_deskripsi
                    new_peminjaman.save()
                except Exception as e:
                    messages += ["Unhandled Exception", ]
                else:
                    return redirect(reverse('peminjaman:index'))

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
        'harga': input_tagihan.__str__(),
        'diskon': input_diskon,
        'nomor_surat': input_nomor_surat,
    })


# Return a form which'll be used to edit peminjaman object to model
@login_required
def formedit(request, peminjaman_id = 0):

    # Berusaha mendapat model peminjam yang ingin diubah
    try:
        selected_peminjaman = Peminjaman.objects.get(id=peminjaman_id)
    except Exception as e:
        return redirect(reverse('peminjaman:index'))

    input_peminjam = selected_peminjaman.peminjam.id
    input_ruangan = selected_peminjaman.ruangan.id
    tanggal_awal = request.POST.get('waktu_awal_0', selected_peminjaman.waktu_awal.date().isoformat())  # format tanggal : %Y-%m-%d
    tanggal_akhir = request.POST.get('waktu_akhir_0', selected_peminjaman.waktu_akhir.date().isoformat())  # format tanggal : %Y-%m-%d
    pukul_awal = request.POST.get('waktu_awal_1', selected_peminjaman.waktu_awal.time().strftime("%H:%M"))  # format waktu : %H:%M
    pukul_akhir = request.POST.get('waktu_akhir_1', selected_peminjaman.waktu_akhir.time().strftime("%H:%M"))  # format waktu : %H:%M
    input_deskripsi = request.POST.get('deskripsi', selected_peminjaman.deskripsi)
    input_tagihan = request.POST.get('harga', selected_peminjaman.jumlah_tagihan)
    input_nomor_surat = request.POST.get('nomor_surat', selected_peminjaman.no_laporan)

    errormsg = []
    messages = []

    if request.method == 'POST':

        # Ambil data pascaedit
        input_tagihan = request.POST['harga']
        input_tagihan = float(input_tagihan)

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

            # Membuat object peminjaman yang sesuai, TIDAK AKAN DI-SAVE
            new_peminjaman = Peminjaman(peminjam=obj_peminjam,
                                        ruangan=obj_ruangan,
                                        waktu_awal=tanggal_mulai_pinjam,
                                        waktu_akhir=tanggal_selesai_pinjam,
                                        deskripsi=input_deskripsi,
                                        jumlah_tagihan=input_tagihan,
                                        no_laporan=input_nomor_surat)

            # Mengecek apakah ada peminjaman yang bentrok,
            collision = new_peminjaman.get_all_conflicted_set()
            collisionset = []
            for peminjaman in collision:
                if not (peminjaman == selected_peminjaman):
                    collisionset += [peminjaman.__str__(), ]

            # Apabila ada bentrok, print semua jadwal yang bentrok, dan kembalikan form
            if (collisionset):
                errormsg += ['Terdapat jadwal yang bentrok :']
                for error in collisionset:
                    errormsg += [error, ]

            # Jika tidak, maka simpan peminjaman, dan kembali ke index
            else:
                try:
                    selected_peminjaman.peminjam = obj_peminjam
                    selected_peminjaman.ruangan = obj_ruangan
                    selected_peminjaman.waktu_awal = tanggal_mulai_pinjam
                    selected_peminjaman.waktu_akhir = tanggal_selesai_pinjam
                    selected_peminjaman.deskripsi = input_deskripsi
                    selected_peminjaman.jumlah_tagihan = input_tagihan
                    selected_peminjaman.no_laporan = input_nomor_surat
                    selected_peminjaman.save()
                except Exception as e:
                    messages += ["Unhandled Exception", ]
                else:
                    return redirect(reverse('peminjaman:index'))

    # Mengembalikan form yang sama
    all_peminjam = Peminjam.objects.all()
    all_ruangan = Ruangan.objects.all()
    return render(request, 'peminjaman/edit.html', {
        'all_peminjam': all_peminjam,
        'all_ruangan': all_ruangan,
        'selected_peminjaman' : selected_peminjaman,
        'error': errormsg,
        'message': messages,
        'input_peminjam': input_peminjam,
        'input_ruangan': input_ruangan,
        'input_deskripsi': input_deskripsi,
        'tanggal_awal': tanggal_awal,
        'pukul_awal': pukul_awal,
        'tanggal_akhir': tanggal_akhir,
        'pukul_akhir': pukul_akhir,
        'harga': input_tagihan.__str__(),
        'nomor_surat': input_nomor_surat,
    })


# Return a form which'll be used to delete peminjaman object to model
@login_required
def formdelete(request, peminjaman_id = 0, errormsg=''):
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


# AJAX Service to toggle pembayaran status
@login_required
@csrf_exempt
def togglepembayaran(request, peminjaman_id = 0):
    if request.method == 'POST':
        # Berusaha mendapat model peminjam yang ingin diubah data pembayarannya
        try:
            selected_peminjaman = Peminjaman.objects.get(id=peminjaman_id)
        except Exception as e:
            return JsonResponse({'result': ""})

        if selected_peminjaman.waktu_bayar:
            selected_peminjaman.waktu_bayar = None
            selected_peminjaman.save()
            return JsonResponse({'result': "Belum Lunas"})

        else:
            selected_peminjaman.waktu_bayar = date.today()
            selected_peminjaman.save()
            return JsonResponse({'result': selected_peminjaman.waktu_bayar})

    return JsonResponse({'result': 'Nope'})


def fetchrecord(request, start_year = 2017):
    selected_peminjaman = Peminjaman.objects.filter(waktu_awal__year = start_year).values()
    return JsonResponse({'results': list(selected_peminjaman)})
