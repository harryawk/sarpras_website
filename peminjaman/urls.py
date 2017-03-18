from django.conf.urls import url
from . import views

app_name = 'peminjaman'

urlpatterns = [
    # /peminjaman/
    url(r'^$', views.index, name='index'),

    # /peminjaman/add/
    url(r'^add/$',views.formadd, name='add'),

]
