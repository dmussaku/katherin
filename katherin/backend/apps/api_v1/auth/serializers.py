# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.users.models import Invite


class LoginSerializer(serializers.Serializer):
    """
    Serializes user's login credentials
    """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)


class InviteSerializer(serializers.Serializer):
    """
    Serializes invites data
    """
    invitee_email = serializers.EmailField(max_length=128)
    authorization = serializers.IntegerField()
    groups = serializers.ListField(child=serializers.IntegerField(), required=False)
    permissions = serializers.ListField(child=serializers.IntegerField(), required=False)

    def create(self, validated_data):
        return Invite.objects.create(**validated_data)
