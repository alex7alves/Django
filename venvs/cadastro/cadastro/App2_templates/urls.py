# -*- coding: utf-8 -*-


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='app2_index'),
    url(r'^(?P<idade>\d+)/$', views.idade, name='app2_idade'),
]