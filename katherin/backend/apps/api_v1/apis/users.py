# -*- coding: utf-8 -*-
"""
API for managing user accounts
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UsersIndex(APIView):
    """
    Handles requests coming to /api/v1/users/
    """
    def post(self, request):
        """
        User account creation with permissions defined in request payload
        """
        pass


class UsersActivate(APIView):
    """
    Handles requests coming to /api/v1/users/activate/
    """
    def post(self, request):
        pass
