# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:54:11
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-08 16:24:08
from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from django.core.mail import send_mail
from django.conf import settings


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

    def update(self, instance, validated_data):
        old_status = instance.status
        instance = super().update(instance, validated_data)
        new_status = instance.status

        if old_status != new_status:
            self.send_status_change_email(instance)
        return instance

    def send_status_change_email(self, order):
        subject = f"Tu pedido #{order.id} ha cambiado de estado"
        message = f"Hola {order.full_name},\n\nEl estado de tu pedido ha cambiado a: {order.status}.\n\nGracias por comprar con nosotros."
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'full_name', 'email', 'phone', 'address', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = validated_data.pop('user', None)  # sacamos user si viene dentro de validated_data
        order = Order.objects.create(user=user, **validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
