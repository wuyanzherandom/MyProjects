#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class AccountAccess(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    value = models.IntegerField(default=0)
    valid_login = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class AccountCategory(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class AccountPermission(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    url = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class AccountGroup(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    account_permission = models.ForeignKey(AccountPermission, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Account(models.Model):
    username = models.CharField(max_length=256, null=False, blank=False, unique=True)
    password = models.CharField(max_length=256, null=False, blank=False)
    email_address = models.CharField(max_length=256, null=True, blank=True)

    account_group = models.ForeignKey(AccountGroup, null=True, blank=True)
    account_category = models.ForeignKey(AccountCategory, null=True, blank=True)

    def __unicode__(self):
        return self.username