# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:54:54
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-08 16:16:36
from django.urls import path
from .views import OrderListCreateAPIView, OrderDetailAPIView, OrderStatusUpdateAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/status/', OrderStatusUpdateAPIView.as_view(), name='order-status-update'),

]
