from django.conf.urls import url
from . import views

app_name = 'peminjaman'

urlpatterns = [

    # /peminjaman/
    url(r'^$', views.index, name='index'),

    # /peminjaman/kalender
    url(r'^kalender/$', views.kalender, name='kalender'),
    url(r'^kalender-umum/$', views.kalender_umum, name='kalender_umum'),

    # /peminjaman/add/
    url(r'^add/$',views.formadd, name='add'),

    # /peminjaman/edit/4
    url(r'^edit/$', views.formedit, name='editbase'),
    url(r'^edit/(?P<peminjaman_id>[0-9]+)/$', views.formedit, name='edit'),

    # /peminjaman/delete/4
    url(r'^delete/$', views.formdelete, name='deletebase'),
    url(r'^delete/(?P<peminjaman_id>[0-9]+)/$', views.formdelete, name='delete'),

    # /peminjaman/json/2016
    url(r'^json/$', views.fetchrecord, name='jsonbase'),
    url(r'^json/(?P<start_year>[0-9]+)/$', views.fetchrecord, name='json'),

    # /peminjaman/bayar/2
    url(r'^bayar/$', views.togglepembayaran, name='bayarbase'),
    url(r'^bayar/(?P<peminjaman_id>[0-9]+)/$', views.togglepembayaran, name='bayar'),
]
