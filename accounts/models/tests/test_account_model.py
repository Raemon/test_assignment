import json

from mock import patch

from django.test import TestCase
from accounts.models import Account, Journal, Ledger, Transaction


# Create your tests here.
class TestAccountModel(TestCase):
    
    def test_create_account_initializes_journals_and_ledgers(self):
        account = Account.objects.create(name="Test User", slug="test-user")
        
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Journal.objects.count(), 1)
        self.assertEqual(Ledger.objects.count(), 2)
        
        journal = Journal.objects.first()
        self.assertEqual(journal.account, account)

        ledgers = Ledger.objects.all()
        self.assertEqual(ledgers[0].journal, journal)
        self.assertEqual(ledgers[1].journal, journal)
        self.assertEqual(ledgers[0].name, Ledger.NAME_CHOICES[0][0])
        self.assertEqual(ledgers[1].name, Ledger.NAME_CHOICES[1][0])
        