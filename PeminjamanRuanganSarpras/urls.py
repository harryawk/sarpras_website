"""PeminjamanRuanganSarpras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^peminjam/', include('peminjam.urls')),
    url(r'^peminjaman/', include('peminjaman.urls')),
    url(r'^ruangan/', include('ruangan.urls')),
    url(r'^log/', include('log.urls')),
    url(r'^login/$', auth_views.login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, kwargs={'next_page': '/login/'}, name='logout'),
    url(r'^$', RedirectView.as_view(pattern_name='peminjaman:kalender_umum', permanent=False), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#    url(r'^admin/', admin.site.urls),

