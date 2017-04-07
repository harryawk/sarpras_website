from django.db import models
from peminjaman.models import Peminjaman

class Log(models.Model):
    peminjaman = models.ForeignKey(Peminjaman, blank=True, null=True, on_delete=models.SET_NULL) #Bernilai null apabila object terkait dihapus
    tanggal = models.DateField(auto_now_add=True, db_index=True)
    deskripsi = models.CharField(blank=True, max_length=1000)

    CREATE = 'Buat'
    UPDATE = 'Ubah'
    DELETE = 'Hapus'
    PILIHAN_TIPE_AKSI = (
        (CREATE, 'Buat'),
        (UPDATE, 'Ubah'),
        (DELETE, 'Hapus'),
    )
    aksi = models.CharField(max_length=50, choices=PILIHAN_TIPE_AKSI, default=UPDATE)


