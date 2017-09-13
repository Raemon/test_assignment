import json

from mock import patch

from django.test import TestCase
from accounts.models import Account, Journal, Ledger, Transaction


# Create your tests here.
class TestTransactionModel(TestCase):
    
    def test_create_transaction_creates_corresponding_entries(self):
        account = Account.objects.create(name="Test User", slug="test-user")
        transaction = Transaction.objects.create(
            account_id=account.id, 
            amount=200
        )
        
        # Transaction
        self.assertEqual(len(account.journal.ledgers.all()[0].entries.all()), 1)
        self.assertEqual(len(account.journal.ledgers.all()[1].entries.all()), 1)
        
    def test_create_transaction_requires_journal_or_account_id(self):
        account = Account.objects.create(name="Test User", slug="test-user")
        with self.assertRaises(ValueError):
            Transaction.objects.create(amount=200), ValueError
            
        transaction_1 = Transaction.objects.create(amount=200, journal_id=1)
        transaction_2 = Transaction.objects.create(amount=200, account_id=1)
        
        self.assertEqual(transaction_1.account.id, 1)
        self.assertEqual(transaction_1.journal.id, 1)
        
        self.assertEqual(transaction_2.account.id, 1)
        self.assertEqual(transaction_2.journal.id, 1)