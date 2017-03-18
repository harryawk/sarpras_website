from django.conf.urls import url
from . import views

app_name = 'peminjam'

urlpatterns = [

    # /peminjam/
    url(r'^$', views.index, name='index'),

    # /peminjam/add/
    url(r'^add/$',views.formadd, name='add'),
    # /peminjam/add/process/
    url(r'^add/process/$', views.processadd, name='processadd'),

    # /peminjam/edit/4
    url(r'^edit/(?P<peminjam_id>[0-9]+)/$', views.formedit, name='edit'),
    # /peminjam/edit/4/process/
    url(r'^edit/(?P<peminjam_id>[0-9]+)/$', views.processedit, name='processedit'),

    # /peminjam/delete/4
    url(r'^delete/(?P<peminjam_id>[0-9]+)/$', views.formdelete, name='delete'),
    # /peminjam/delete/4/process/
    url(r'^delete/(?P<peminjam_id>[0-9]+)/$', views.processdelete, name='processdelete'),
]
