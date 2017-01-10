# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import Group


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
    email = models.EmailField(verbose_name='email address', max_length=128, unique=True, null=False)
    token = models.CharField(max_length=128, null=True, unique=True)
    first_name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)
    phone = models.CharField(max_length=40, null=True)
    is_accepted = models.NullBooleanField(null=True)
    is_active = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    inviter_id = models.IntegerField(null=True)
    date_invited = models.DateTimeField(null=True)

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