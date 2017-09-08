import json

from django.test import TestCase
from django.test import Client
from accounts.models import Account, Journal, Ledger, Transaction

# Create your tests here.
class TestAccounts(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.maxDiff = None
        
    def test_create_account_initializes_journal_and_ledgers(self):
        name = "Test User"
        
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Journal.objects.count(), 1)
        self.assertEqual(Ledger.objects.count(), 2)
        
        account = Account.objects.first()
        self.assertEqual(account.name, name)
        
        journal = Journal.objects.first()
        self.assertEqual(journal.account, account)

        ledgers = Ledger.objects.all()
        self.assertEqual(ledgers[0].journal, journal)
        self.assertEqual(ledgers[1].journal, journal)
        self.assertEqual(ledgers[0].name, Ledger.NAME_CHOICES[0][0])
        self.assertEqual(ledgers[1].name, Ledger.NAME_CHOICES[1][0])
        
    def test_create_account_returns_account_id(self):
        response = self.client.post("/accounts", {'name': 'Test User', 'slug': 'test-user'})
        self.assertEqual(json.loads(response.content), {'id':1})

    def test_get_account_returns_custom_fields(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug': 'test-user'})
        response = self.client.get("/accounts/1")
        
        expected_output = {
            'id':1,
            'principal':0,
            'transactions':[]
        }
        
        self.assertEqual(json.loads(response.content), expected_output)
        
        self.client.post("/transactions", {'account': 'test-user', 'amount':200})
        self.client.post("/transactions", {'account': 'test-user', 'amount':50})
        
        output = json.loads(self.client.get("/accounts/1").content)
        
        self.assertEqual(output['id'], 1)
        self.assertEqual(output['principal'], 250.0)
        self.assertEqual(output['transactions'].__len__(), 2)
        
        self.assertIsNotNone(output['transactions'][0]['timestamp'])
        self.assertEqual(output['transactions'][0]['type'], 'purchase')
        self.assertEqual(output['transactions'][0]['amount'], '200.0000000000')

        self.assertEqual(output['transactions'][1]['type'], 'purchase')
        self.assertIsNotNone(output['transactions'][1]['timestamp'])
        