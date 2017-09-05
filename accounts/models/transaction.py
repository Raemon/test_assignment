from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin
from .ledger import Ledger

class Transaction(TimeStampMixin, IsEnabledMixin):
    PURCHASE = 'purchase'

    TRANSACTION_TYPE_CHOICES = (
        (PURCHASE, 'Purchase'),
    )
    
    transaction_type = models.CharField(
        max_length=200,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    ledger = models.ForeignKey(Ledger)