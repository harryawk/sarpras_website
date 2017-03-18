from django.shortcuts import render


def index(request):
    return render(request, 'peminjam/index.html', {})


def formadd(request):
    return render(request, 'peminjam/add.html', {})
