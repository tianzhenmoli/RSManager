"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^psd2png/$', views.psd_to_png, name='psd2png'),
    url(r'^chdir/$', views.web_change_dir, name='chdir'),
    url(r'^zipfile/$', views.zip_download, name='zipfile'),
    url(r'^download_file/(?P<zname>[^/]+)/$', views.downloadfile, name='download'),
    url(r'^resources/(?P<dir1>[^/]+)/$', views.show_multilayer_dir, name='show_dir_1'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/$', views.show_multilayer_dir, name='show_dir_2'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/$', views.show_multilayer_dir, name='show_dir_3'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/$', views.show_multilayer_dir, name='show_dir_4'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/(?P<dir5>[^/]+)/$', views.show_multilayer_dir, name='show_dir_5'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/(?P<dir5>[^/]+)/(?P<dir6>[^/]+)/$', views.show_multilayer_dir, name='show_dir_6'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/(?P<dir5>[^/]+)/(?P<dir6>[^/]+)/(?P<dir7>[^/]+)/$',
        views.show_multilayer_dir, name='show_dir_7'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/(?P<dir5>[^/]+)/(?P<dir6>[^/]+)/(?P<dir7>[^/]+)/(?P<dir8>[^/]+)/$',
        views.show_multilayer_dir, name='show_dir_8'),
    url(r'^resources/(?P<dir1>[^/]+)/(?P<dir2>[^/]+)/(?P<dir3>[^/]+)/(?P<dir4>[^/]+)/(?P<dir5>[^/]+)/(?P<dir6>[^/]+)/(?P<dir7>[^/]+)/(?P<dir8>[^/]+)/(?P<dir9>[^/]+)/$',
        views.show_multilayer_dir, name='show_dir_9'),
]
