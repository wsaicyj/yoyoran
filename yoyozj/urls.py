#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import index, fresh_food


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^fresh_food/$', fresh_food, name='fresh_food'),
]