# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

from ..CommonDB import models as CommonDBModel

# use to lock transaction or multi action
class Lock(CommonDBModel.TimeRecord):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True, db_index=True)
    counter = models.BigIntegerField(blank=False, null=False, default=0)

    class Meta:
        verbose_name = _('Lock')


# user info
class Member(CommonDBModel.TimeRecord):
    pass


# store transaction record
class TransactionBase(CommonDBModel.TimeRecord):
    ref_no = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Reference No."))
    from_member = models.ForeignKey("Member", null=True, blank=True, verbose_name=_("From Member"))
    to_member = models.ForeignKey("Member", null=True, blank=True, verbose_name=_("To Member"))
    transaction_date = models.DateTimeField(null=False, blank=False, verbose_name=_("Transaction Date")) #, auto_now_add=True)
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Amount"))
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="New balance after this transaction")

    class Meta:
        verbose_name = _("Transaction")
        abstract = True