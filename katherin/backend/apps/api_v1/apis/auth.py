# -*- coding: utf-8 -*-
"""
API for authorithing/authenticating requests
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# from .serializers.auth_serializer import *


class AuthIndex(APIView):
    """
    Handles requests coming to /api/v1/auth/ - user authentication
    """
    def post(self, request):
        pass
