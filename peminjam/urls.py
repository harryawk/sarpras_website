from django.conf.urls import url
from . import views

app_name = 'peminjam'

urlpatterns = [

    # /peminjam/
    url(r'^$', views.index, name='index'),

    # /peminjam/add/
    url(r'^add/$',views.formadd, name='add'),

    # /peminjaman/add/process/
    url(r'^add/process/$', views.processadd, name='processadd'),
]
