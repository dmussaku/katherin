# -*- coding: utf-8 -*-
"""
API for managing invitation for accessing portals
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.invites_serializer import InviteSerializer
from utils.security_utils import generate_token


class InvitesIndex(APIView):
    """
    Handles requests coming to /api/v1/invites/
    """
    def post(self, request):
        """
        Creating invite entry in system
        """
        serializer = InviteSerializer(data=request.data)
        if not serializer.is_valid():
            content = {
                'success': False,
                'errors': serializer.errors
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        try:
            invite = serializer.save(inviter=request.user, token=generate_token())
        except Exception as e:
            # TODO: Log to Sentry
            content = {
                'success': False,
                'detail': 'Could not create invite.'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        content = {
            'success': True
        }
        return Response(content)


class UsersActivate(APIView):
    """
    Handles requests coming to /api/v1/users/activate/
    """
    def post(self, request):
        pass
