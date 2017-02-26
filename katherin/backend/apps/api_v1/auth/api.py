# -*- coding: utf-8 -*-
"""
API for authorithing/authenticating requests
"""
from django.contrib import auth
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied

from utils.security_utils import generate_token
from apps.users.models import CustomUser
from .serializers import LoginSerializer, InviteSerializer


class AuthViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny, )

    @list_route(methods=['post'], url_path='login')
    def login(self, request):
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
            raise PermissionDenied
        content = {
            'success': True
        }
        return Response(content)

    @list_route(methods=['post'], url_path='invite')
    def invite(self, request):
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

    @detail_route(methods=['post'], url_path='activate_user')
    def activate_user(self, request, pk=None):
        '''
        TODO
        '''
        return Response()

# class UsersIndex(APIView):
#     """
#     Handles requests coming to /api/v1/users/
#     """
#     def post(self, request):
#         """
#         User account creation with permissions defined in request payload
#         """
#         pass


# class UsersActivate(APIView):
#     """
#     Handles requests coming to /api/v1/users/activate/
#     """
#     def post(self, request):
#         pass
