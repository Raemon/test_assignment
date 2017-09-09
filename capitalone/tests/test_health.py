from django.test import TestCase
from django.test import Client
from accounts.models import Account, Journal, Ledger, Transaction

# Create your tests here.
class TestAccounts(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_create_account_creates_(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
