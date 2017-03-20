from django.db import models
from ruangan.models import Ruangan
from peminjam.models import Peminjam


class Peminjaman(models.Model):
    peminjam = models.ForeignKey(Peminjam,on_delete=models.CASCADE, db_index=True)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE, db_index=True)
    waktu_awal = models.DateTimeField(auto_now=False, auto_now_add=False, db_index=True)
    waktu_akhir = models.DateTimeField(auto_now=False, auto_now_add=False, db_index=True)
    deskripsi = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return (self.peminjam.__str__() +' : '+ self.ruangan.__str__() +', '+ self.waktu_awal.__str__() +' -> '+ self.waktu_akhir.__str__())


class Pembayaran(models.Model):
    peminjaman = models.ForeignKey(Peminjaman,on_delete=models.CASCADE, db_index=True)
    waktu_bayar = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    deskripsi = models.CharField(max_length=1000, blank=True)

    BELUM_BAYAR = 'B'
    SUDAH_LUNAS = 'S'
    PILIHAN_STATUS_BAYAR = (
        (BELUM_BAYAR, 'Belum Lunas'),
        (SUDAH_LUNAS, 'Sudah Lunas'),
    )
    tipe = models.CharField(max_length=50, choices=PILIHAN_STATUS_BAYAR, default=BELUM_BAYAR, db_index=True)