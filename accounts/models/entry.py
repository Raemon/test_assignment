from django.db import models
from common.mixins import TimeStampMixin, IsEnabledMixin
from .ledger import Ledger

class Entry(TimeStampMixin, IsEnabledMixin):
    ledger = models.ForeignKey(Ledger, related_name='entries')
    amount = models.DecimalField(max_digits=19, decimal_places=10)
