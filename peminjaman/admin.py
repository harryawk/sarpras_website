from django.contrib import admin
from .models import Peminjaman, Pembayaran

admin.site.register(Peminjaman)
admin.site.register(Pembayaran)
