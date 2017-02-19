# -*- coding: utf-8 -*-
"""
API for authorithing/authenticating requests
"""
from django.contrib import auth
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied

from .serializers.auth_serializer import *


class AuthIndex(APIView):
    """
    Handles requests coming to /api/v1/auth/ - user authentication
    """
    # This API endpoint has to circumvent default SessionAuthentication for all requests
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            content = {
                'success': False,
                'errors': serializer.errors
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
        else:
            # Don't return any sensible 
            raise PermissionDenied
        content = {
            'success': True
        }
        return Response(content)
