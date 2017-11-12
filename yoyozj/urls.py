#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import index, freshfood


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^freshfood/$', freshfood, name='freshfood'),
]