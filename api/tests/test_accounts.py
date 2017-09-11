import json

from mock import patch

from django.test import TestCase
from django.test import Client
from accounts.models import Account, Journal, Ledger, Transaction


# Create your tests here.
class TestAccountSerializer(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.maxDiff = None
        
    @patch('accounts.models.account.AccountManager.create')
    def test_post_account_calls_account_manager_create(self, create):
        name = "Test User"
        slug = "test-user"
        
        self.client.post("/accounts", {'name': name, 'slug':slug})
        create.assert_called_with(name=name, slug=slug)
        
    def test_create_account_returns_account_id(self):
        response = self.client.post("/accounts", {'name': 'Test User', 'slug': 'test-user'})
        self.assertEqual(json.loads(response.content), {'id':1})
        
    def test_create_account_requires_name(self):
        response = self.client.post("/accounts", {'slug': 'test-user'})
        self.assertEqual(json.loads(response.content), {'name': ['This field is required.']})

    def test_create_account_requires_slug(self):
        response = self.client.post("/accounts", {'name': 'Test User'})
        self.assertEqual(json.loads(response.content), {'slug': ['This field is required.']})

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
        self.assertEqual(output['transactions'][0]['amount'], 200)

        self.assertEqual(output['transactions'][1]['type'], 'purchase')
        self.assertIsNotNone(output['transactions'][1]['timestamp'])
        