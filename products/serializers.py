# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-08 14:18:27
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-08 14:44:12
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
