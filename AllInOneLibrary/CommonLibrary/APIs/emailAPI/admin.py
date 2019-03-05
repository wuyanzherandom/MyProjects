#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

@admin.register(models.EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    pass