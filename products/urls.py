# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:19:18
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-08 14:44:34
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
