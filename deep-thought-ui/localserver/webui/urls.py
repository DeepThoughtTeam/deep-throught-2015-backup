"""localserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'webui.views.home', name='home'),
    url(r'^show-train-result/$', 'webui.views.show_train_result', name='show_train_res'),
    url(r'^show-test-result/$', 'webui.views.show_test_result', name='show_test_res'),


    url(r'^caffe-train-result/$', 'webui.views.caffe_train_result', name='caffe_train_res'),
    url(r'^caffe-test-result/$', 'webui.views.caffe_test_result', name='caffe_test_res'),

    url(r'^upload_file/$', 'webui.views.upload_file', name ='upload_file'),

    url(r'^net-description/$', 'webui.views.net_description', name='net_description'),

    url(r'^display-net/$', 'webui.views.display_net', name='display_net'),

    url(r'^beautiful-home/$', 'webui.views.beautiful_home', name='beautiful_home'),

    url(r'^train/$', 'webui.views.train', name='train'),

    url(r'^test/$', 'webui.views.test', name='test'),
]

