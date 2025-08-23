# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-19 22:20:03
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-19 22:20:16
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser"]
