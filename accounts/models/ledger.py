from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin
from .journal import Journal

class Ledger(TimeStampMixin, IsEnabledMixin):
    CASHOUT = 'cashout'
    PRINCIPAL = 'principal'

    LEDGER_TYPE_CHOICES = (
        (CASHOUT, 'Cash Out'),
        (PRINCIPAL, 'Principal'),
    )    
    
    journal = models.ForeignKey(Journal)
    ledger_type = models.CharField(
        max_length=200,
        choices=LEDGER_TYPE_CHOICES,
    )
