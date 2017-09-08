from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin
from .journal import Journal

class Ledger(TimeStampMixin, IsEnabledMixin):
    CASHOUT = 'cashout'
    PRINCIPAL = 'principal'

    NAME_CHOICES = (
        (CASHOUT, 'Cash Out'),
        (PRINCIPAL, 'Principal'),
    )    
    
    journal = models.ForeignKey(Journal, related_name='ledgers')
    
    name = models.CharField(
        max_length=200,
        choices=NAME_CHOICES,
    )
