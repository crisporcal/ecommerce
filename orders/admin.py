# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:50:37
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-19 09:47:06
from django.contrib import admin
from .models import Order, OrderItem
from .utils import send_order_status_email

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    inlines = [OrderItemInline]
    list_editable = ['status']  # <- esto permite editar el estado directamente en la lista

    def save_model(self, request, obj, form, change):
        if change:  # Si es una edición
            previous = Order.objects.get(pk=obj.pk)
            if previous.status != obj.status:
                send_order_status_email(obj)  # Enviar email solo si cambió el estado
        super().save_model(request, obj, form, change)
