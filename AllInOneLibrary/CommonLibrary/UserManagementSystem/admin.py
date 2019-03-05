#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from . import models


class AccountPermissionInline(admin.TabularInline):
    model = models.AccountPermission


class AccountGroupAdmin(admin.ModelAdmin):
    inlines = [AccountPermissionInline,]


@admin.register(models.AccountGroup)
class AccountGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AccountPermission)
class AccountPermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    pass