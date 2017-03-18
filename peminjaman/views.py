from django.shortcuts import render


def index(request):
    return render(request, 'peminjaman/index.html', {})


def formadd(request):
    return render(request, 'peminjaman/add.html', {})
