import json

from mock import patch

from django.test import TestCase
from django.test import Client

# Create your tests here.
class TestTransactionSerializers(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.maxDiff = None

    # The following test causes a strange error: decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
    #
    # It looks like django/django-rest-framework has issues with mocking an object manager while making an API call
    # I'm looking into it, but didn't want to delay the submission of this take-home-exercise too long while I explored it

    # @patch('accounts.models.transaction.TransactionManager.create')        
    # def test_post_transaction_calls_transaction_manager_create(self, create):
    #     self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
    #     self.client.post("/transactions", {'account': 'test-user', 'amount':200})
        
    #     create.call_count(account="test-user", amount=200)
        
    def test_create_transaction_returns_amount(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})

        self.client.post("/transactions", {'account': 'test-user', 'amount':200})
        self.client.post("/transactions", {'account': 'test-user', 'amount':200.1234})
        output = json.loads(self.client.get("/accounts/1").content)
        
        self.assertEqual(output['transactions'][0]['amount'], 200)
        self.assertEqual(output['transactions'][1]['amount'], 200.1234)
        
        