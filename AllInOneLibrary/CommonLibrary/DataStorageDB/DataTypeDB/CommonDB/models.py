# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# use to record time create or modified every model save
class TimeRecord(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Time"))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_("Modified Time"))
    active_status = models.BooleanField(default=True, verbose_name=_("Active Status"))  # true - allow to use
    comment = models.TextField(blank=True, null=True, verbose_name=_("Comments"))
    #user = models.ForeignKey(User, default='', null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        verbose_name = _('TimeRecord')