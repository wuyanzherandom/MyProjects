#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class EmailModel(models.Model):

    title = models.CharField(max_length=256, null=False, blank=False)
    body = models.TextField(null=True, blank=True)
    from_who = models.CharField(max_length=256, null=False, blank=False)
    to_who = models.CharField(max_length=256, null=False, blank=False)

    def __unicode__(self):
        return self.title