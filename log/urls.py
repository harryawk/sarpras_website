from django.conf.urls import url
from . import views

app_name = 'log'

urlpatterns = [

    # /log/
    url(r'^$', views.index, name='index'),

]
