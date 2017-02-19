# -*- coding: utf-8 -*-
"""
Models for users accounts management
    models: CustomUser, Invite
"""
from datetime import timedelta

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from utils.security_utils import generate_token
from utils.exceptions import CreateInstanceException


class CustomUserManager(BaseUserManager):
    """
    """
    def create_user(self, email, first_name='', last_name='', password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, name, surname and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Redefines Django's default User model
    """
    GUEST = 1
    PARTICIPANT = 2
    ADMIN = 3
    AUTHORIZATION = (
        (GUEST, 'Guest'),
        (PARTICIPANT, 'Participant'),
        (ADMIN, 'Admin')
        )
    email = models.EmailField(verbose_name='email address', max_length=128, unique=True, null=False)
    token = models.CharField(max_length=128, null=True, unique=True)
    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=40, null=True)
    is_accepted = models.NullBooleanField(null=True)
    is_active = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    inviter_id = models.IntegerField(null=True)
    date_invited = models.DateTimeField(null=True)
    authorization = models.PositiveSmallIntegerField(choices=AUTHORIZATION, null=False, default=1)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):

        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):

        return self.first_name

    def __str__(self): 

        return self.email

    def __repr__(self):
        return '<CustomUser %r>' % self.email


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
    groups = ArrayField(models.IntegerField(), null=True) # Groups invitee has access to to
    permissions = ArrayField(models.IntegerField(), null=True) # Permissions invitee has access to

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
