# -*- coding: utf-8 -*-
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    Serializes user's login credentials
    """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)
