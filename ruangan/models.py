from django.db import models

class Ruangan(models.Model):

    nama = models.CharField(max_length=250, unique=True, db_index=True)
    harga = models.BigIntegerField(default=0)
    deskripsi = models.CharField(max_length=1000, blank=True)

    RUANG = 'R'
    SELASAR = 'S'
    LAPANGAN = 'L'
    PILIHAN_TIPE_RUANG = (
        (RUANG, 'Ruang'),
        (SELASAR, 'Selasar'),
        (LAPANGAN, 'Lapangan'),
    )
    tipe = models.CharField(max_length=50, choices=PILIHAN_TIPE_RUANG, default=SELASAR)


    def __str__(self):
        return self.nama + ' - ' + self.tipe