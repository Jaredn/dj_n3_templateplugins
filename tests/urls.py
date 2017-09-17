# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from dj_n3_templateplugins.urls import urlpatterns as dj_n3_templateplugins_urls

urlpatterns = [
    url(r'^', include(dj_n3_templateplugins_urls, namespace='dj_n3_templateplugins')),
]
