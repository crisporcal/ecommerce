# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:50:37
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-08 16:16:03
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Permitimos que cualquiera cree pedido
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'full_name', 'email']  # campos que querés filtrar

    def get_serializer_context(self):
        # Pasamos la request al serializer para acceder al usuario
        return {'request': self.request}

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            # Admin puede ver todos los pedidos
            return Order.objects.all()
        elif user.is_authenticated:
            # Usuarios normales solo ven sus pedidos
            return Order.objects.filter(user=user)
        else:
            # Usuarios no autenticados no ven pedidos
            return Order.objects.none()
        
    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)
    
class OrderStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]  # Solo admin puede cambiar estado
    http_method_names = ['patch']  # Solo permitimos PATCH

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True  # Permite actualización parcial
        return super().get_serializer(*args, **kwargs)