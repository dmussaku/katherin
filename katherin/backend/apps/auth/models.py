from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

from apps.users.models import CustomUser
from utils.security_utils import generate_token
from utils.exceptions import CreateInstanceException


class Invite(models.Model):
    """
    Invitation token management model
    """
    token = models.CharField(max_length=64)
    date_create = models.DateField(auto_now_add=True)
    date_expire = models.DateField(default=timezone.now() + timedelta(days=7))
    inviter = models.ForeignKey(CustomUser, models.DO_NOTHING)
    invitee_email = models.EmailField(max_length=256)
    authorization = models.PositiveSmallIntegerField(default=2) # Defines whether invitee is Guest, Participant or Admin
    groups = models.ArrayField(models.IntegerField(), required=False) # Groups invitee has access to to
    permissions = models.ArrayField(models.IntegerField(), required=False) # Permissions invitee has access to

    @classmethod
    def create(cls, request, email, authorization, groups=None, permissions=None):
    	"""
    	Create Invite instance
    	"""
    	invite_token = cls(
    		token=generate_token(),
    		inviter=request.user,
    		invitee_email=email,
    		authorization=authorization,
    		groups=groups,
    		permissions=permissions
    		)
    	try:
    		invite_token.save()
    	except Exception as e:
    		# TODO: Send exception to Sentry
    		raise CreateInstanceException('Could not create invite token.')

    	return invite_token

