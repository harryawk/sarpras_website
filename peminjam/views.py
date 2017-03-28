from django.shortcuts import render, redirect
from .models import Peminjam
from django.urls import reverse


# Peminjam index view, mostly for debugging purpose
def index(request, message='', error=''):
    all_peminjam = Peminjam.objects.all()
    return render(request, 'peminjam/index.html', {
        'error': error,
        'message': message,
        'all_peminjam': all_peminjam
    })


# Return a form which'll be used to add new Peminjam object to model
def formadd(request):

    # Inisiasi variabel berdasarkan post jika ada
    new_nama = request.POST.get("nama",'')
    new_deskripsi = request.POST.get("deskripsi",'')
    error = []
    message = []

    if new_nama == '' and request.method == 'POST':
        error += ["Nama organisasi tidak boleh kosong", ]

    # Jika ada data post yang diberikan,
    if not error and request.method == 'POST':

        # Mengecek apakah ada object dengan nama yang sama
        if (Peminjam.objects.filter(nama=new_nama)):
            error += ["Sudah ada data peminjam dengan nama yang sama", ]

        # Berusaha memasukan object ke database jika tidak ada error
        if not error:
            new_peminjam = Peminjam(
                nama=new_nama,
                deskripsi=new_deskripsi
            )

            # Berusaha menyimpan perubahan dan redirect ke Index jika berhasil
            try:
                new_peminjam.save()
            except Exception as e:
                message += ["Unhandled Exception", ]
            else:
                return redirect(reverse('peminjam:index'))

    # Mengembalikan form yang sama
    return render(request, 'peminjam/add.html', {
        'error': error,
        'message': message,
        'nama': new_nama,
        'deskripsi': new_deskripsi
    })


# Return a form which'll be used to edit Peminjam object to model
def formedit(request, peminjam_id):

    # Berusaha mendapat model peminjam yang ingin diubah
    try:
        selected_peminjam = Peminjam.objects.get(id=peminjam_id)
    except Exception as e:
        return redirect(reverse('peminjam:index'))

    # Inisiasi variabel berdasarkan post jika ada
    new_nama = request.POST.get("nama",'')
    new_deskripsi = request.POST.get("deskripsi",'')
    error = []
    message = []

    if new_nama == '' and request.method == 'POST':
        error += ["Nama organisasi tidak boleh kosong", ]

    # Jika ada data post yang diberikan,
    if not error and request.method == 'POST':

        # Mengecek apakah ada object dengan nama yang sama
        if (Peminjam.objects.filter(nama=new_nama) and (not(selected_peminjam.nama == new_nama))):
            error += ["Sudah ada data peminjam dengan nama yang sama", ]

        # Berusaha mengubah informasi object jika tidak ada error
        if not error:
            selected_peminjam.nama = new_nama
            selected_peminjam.deskripsi = new_deskripsi

            # Berusaha menyimpan perubahan dan redirect ke Index jika berhasil
            try:
                selected_peminjam.save()
            except Exception as e:
                message += ["Unhandled Exception", ]
            else:
                return redirect(reverse('peminjam:index'))


    # Mengembalikan form yang sama
    return render(request, 'peminjam/edit.html', {
        'selected_peminjam': selected_peminjam,
        'error': error,
        'message': message,
    })


# Return a form which'll be used to delete Peminjam object to model
def formdelete(request, peminjam_id):

    # Berusaha mendapat model peminjam yang ingin diubah
    try:
        selected_peminjam = Peminjam.objects.get(id=peminjam_id)
    except Exception as e:
        return redirect(reverse('peminjam:index'))

    # Inisiasi variabel berdasarkan post jika ada
    new_nama = request.POST.get("nama",'')
    error = []
    message = []

    # Jika ada data post yang diberikan,
    if(new_nama):

        # Mengecek apakah ada object dengan nama yang sama
        if (not(selected_peminjam.nama == new_nama)):
            error += ["Nama peminjam tidak sama", ]

        # Berusaha mengubah informasi object jika tidak ada error
        if not error:

            # Berusaha menyimpan perubahan dan redirect ke Index jika berhasil
            try:
                selected_peminjam.delete()
            except Exception as e:
                message += ["Unhandled Exception", ]
            else:
                return redirect(reverse('peminjam:index'))

    # Mengembalikan form yang sama
    return render(request, 'peminjam/delete.html', {
        'selected_peminjam': selected_peminjam,
        'error': error,
        'message': message,
    })

