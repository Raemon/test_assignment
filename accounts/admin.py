# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account, Journal, Ledger, Transaction

class AccountAdmin(admin.ModelAdmin):
    pass

class JournalAdmin(admin.ModelAdmin):
    pass
    
class LedgerAdmin(admin.ModelAdmin):
    pass
    
class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Ledger, LedgerAdmin)
admin.site.register(Transaction, TransactionAdmin)
