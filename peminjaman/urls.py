from django.conf.urls import url
from . import views

app_name = 'peminjaman'

urlpatterns = [

    # /peminjaman/
    url(r'^$', views.index, name='index'),

    # /peminjaman/add/
    url(r'^add/$',views.formadd, name='add'),
    # /peminjaman/add/process/
    url(r'^add/process/$', views.processadd, name='processadd'),

    # /peminjaman/edit/4
    url(r'^edit/(?P<peminjaman_id>[0-9]+)/$', views.formedit, name='edit'),
    # /peminjaman/edit/4/process/
    url(r'^edit/(?P<peminjaman_id>[0-9]+)/$', views.processedit, name='processedit'),

    # /peminjaman/delete/4
    url(r'^delete/(?P<peminjaman_id>[0-9]+)/$', views.formdelete, name='delete'),
    # /peminjaman/delete/4/process/
    url(r'^delete/(?P<peminjaman_id>[0-9]+)/$', views.processdelete, name='processdelete'),
]
