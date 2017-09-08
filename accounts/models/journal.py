from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin
from .account import Account
        
class JournalManager(models.Manager):
    
    def create(self, **kwargs):
        from .ledger import Ledger
    
        with transaction.atomic():
            journal = self.model(**kwargs)
            journal.save(force_insert=True)
            Ledger.objects.create(name=Ledger.CASHOUT, journal=journal)
            Ledger.objects.create(name=Ledger.PRINCIPAL, journal=journal)
        return journal
    
        
class Journal(TimeStampMixin, IsEnabledMixin): 
    account = models.OneToOneField(Account, related_name='journal')
    
    objects = JournalManager()