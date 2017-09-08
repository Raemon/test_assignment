import django.db 

# note: importing django.db to call django.db.transaction without confusing it with our new Transaction type

from django.db import models
from common.mixins import TimeStampMixin, IsEnabledMixin
from .journal import Journal
from .account import Account
from .entry import Entry

# note: be sure not to confuse the django transaction module (used to manipulate database sessions)
# and bank transactions. (here we are importing django.db and calling django.db.transaction to avoid confusion)


class TransactionManager(models.Manager):
    
    def create(self, **kwargs):
        with django.db.transaction.atomic():
            transaction = self.model(**kwargs)
            transaction.save(force_insert=True)
            
            for ledger in transaction.journal.ledgers.all():
                Entry.objects.create(
                    amount=transaction.amount,
                    ledger=ledger
                )
        return transaction


class Transaction(TimeStampMixin, IsEnabledMixin):
    PURCHASE = 'purchase'

    TRANSACTION_TYPE_CHOICES = (
        (PURCHASE, 'Purchase'),
    )
    
    transaction_type = models.CharField(
        max_length=200,
        choices=TRANSACTION_TYPE_CHOICES,
        default=PURCHASE
    )
    
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    journal = models.ForeignKey(Journal, related_name="transactions")
    account = models.ForeignKey(Account, related_name="transactions")

    objects = TransactionManager()