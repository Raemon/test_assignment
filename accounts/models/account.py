from django.db import models, transaction
from common.mixins import TimeStampMixin, IsEnabledMixin, NameSlugMixin

class AccountManager(models.Manager):
    
    def create(self, **kwargs):
        # Avoids circular import
        from .journal import Journal
        with transaction.atomic():
            account = self.model(**kwargs)
            account.save(force_insert=True)
            Journal.objects.create(account=account)
        return account


class Account(TimeStampMixin, IsEnabledMixin, NameSlugMixin):
    
    objects = AccountManager()