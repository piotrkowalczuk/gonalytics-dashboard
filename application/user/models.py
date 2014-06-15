# -*- coding: utf-8 -*-
from django.db import models
from user.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __unicode__(self):
        return self.get_fullname()

    def get_fullname(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
