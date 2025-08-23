# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-22 10:50:53
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-22 10:50:56
from django.urls import path
from .views import get_me

urlpatterns = [
    path("me/", get_me, name="get_me"),
]
