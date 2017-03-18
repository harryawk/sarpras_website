from django.conf.urls import url
from . import views

app_name = 'ruangan'

urlpatterns = [
    # /ruangan/
    url(r'^$', views.index, name='index'),

    # /ruangan/add/
    url(r'^add/$',views.formadd, name='add'),

]
