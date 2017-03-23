from django.shortcuts import render, redirect
from .models import Ruangan
from django.urls import reverse


# Ruangan index view, mostly for debugging purpose
def index(request):
    all_ruangan = Ruangan.objects.all()
    return render(request, 'ruangan/index.html', {
        'all_ruangan': all_ruangan
    })


# Return a form which'll be used to add new Ruangan object to model
def formadd(request):
	
	# Inisiasi variabel berdasarkan post jika ada
    new_nama = request.POST.get("nama",'')
    new_harga = request.POST.get("harga",'')
    new_deskripsi = request.POST.get("deskripsi", '')
    new_tipe = request.POST.get("tipe", '')
	
    error = []
    message = []

    # Jika ada data post yang diberikan,
    if(new_nama and new_harga and new_deskripsi and new_tipe):

        # Mengecek apakah ada object dengan nama yang sama
        if (Ruangan.objects.filter(nama=new_nama)):
            error += ["Sudah ada data ruangan dengan nama yang sama", ]

        # Berusaha memasukan object ke database jika tidak ada error
        if not error:
            new_ruangan = Ruangan(
                nama = new_nama,
				harga = new_harga,
                deskripsi = new_deskripsi,
				tipe = new_tipe
            )

            # Berusaha menyimpan perubahan dan redirect ke Index jika berhasil
            try:
                new_ruangan.save()
            except Exception as e:
                message += ["Unhandled Exception", ]
            else:
                return redirect(reverse('ruangan:index'))

    # Mengembalikan form yang sama
    return render(request, 'ruangan/add.html', {
        'error': error,
        'message': message,
        'nama': new_nama,
		'harga': new_harga,
        'deskripsi': new_deskripsi,
		'tipe': new_tipe
    })


# Return a form which'll be used to edit Ruangan object to model
def formedit(request, ruangan_id):
    return render(request, 'ruangan/edit.html', {})


# Return a form which'll be used to delete Ruangan object to model
def formdelete(request, ruangan_id):
    return render(request, 'ruangan/delete.html', {})

