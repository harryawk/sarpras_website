from django.conf.urls import url
from . import views

app_name = 'ruangan'

urlpatterns = [

    # /ruangan/
    url(r'^$', views.index, name='index'),

    # /ruangan/add/
    url(r'^add/$', views.formadd, name='add'),
    # /ruangan/add/process/
    url(r'^add/process/$', views.processadd, name='processadd'),

    # /ruangan/edit/4
    url(r'^edit/(?P<ruangan_id>[0-9]+)/$', views.formedit, name='edit'),
    # /ruangan/edit/4/process/
    url(r'^edit/(?P<ruangan_id>[0-9]+)/$', views.processedit, name='processedit'),

    # /ruangan/delete/4
    url(r'^delete/(?P<ruangan_id>[0-9]+)/$', views.formdelete, name='delete'),
    # /ruangan/delete/4/process/
    url(r'^delete/(?P<ruangan_id>[0-9]+)/$', views.processdelete, name='processdelete'),

]
