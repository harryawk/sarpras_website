from django.conf.urls import url
from . import views

app_name = 'peminjaman'

urlpatterns = [

    # /peminjaman/
    url(r'^$', views.index, name='index'),

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
]
