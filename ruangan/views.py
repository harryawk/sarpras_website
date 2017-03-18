from django.shortcuts import render


def index(request):
    return render(request, 'ruangan/index.html', {})


def formadd(request):
    return render(request, 'ruangan/add.html', {})
