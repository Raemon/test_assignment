from django.test import TestCase
from django.test import Client
from accounts.models import Account, Journal, Ledger, Transaction

# Create your tests here.
class TestAccounts(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_create_account(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug': 'test-user'})
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Journal.objects.count(), 1)
        self.assertEqual(Ledger.objects.count(), 2)
        