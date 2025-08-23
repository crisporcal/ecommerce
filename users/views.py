# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-19 22:17:08
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-22 11:29:28
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role
    })



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Añadir role al token
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
