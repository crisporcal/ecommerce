# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-19 22:17:08
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-22 10:40:01
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('partner', 'Partner'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f"{self.username} ({self.role})"
