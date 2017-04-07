from django.shortcuts import render, redirect, reverse

# Log index view
def index(request):
    return redirect(reverse('ruangan:index'))