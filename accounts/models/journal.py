from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin
from .account import Account
        
class JournalManager(models.Manager):
    
    def create(self, **kwargs):
        from .ledger import Ledger
    
        with transaction.atomic():
            journal = self.model(**kwargs)
            journal.save(force_insert=True)
            Ledger.objects.create(ledger_type=Ledger.CASHOUT, journal=journal)
            Ledger.objects.create(ledger_type=Ledger.PRINCIPAL, journal=journal)
        return journal
    
        
class Journal(TimeStampMixin, IsEnabledMixin): 
    account = models.ForeignKey(Account)
    
    objects = JournalManager()