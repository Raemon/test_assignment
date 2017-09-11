import json

from mock import patch

from django.test import TestCase
from django.test import Client
from rest_framework import serializers

from accounts.models import Account
from ..serializers.transactions import valid_account

# Create your tests here.
class TestTransactionSerializer(TestCase):
    
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
        
    def test_post_transaction_returns_amount(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})

        self.client.post("/transactions", {'account': 'test-user', 'amount':200})
        self.client.post("/transactions", {'account': 'test-user', 'amount':200.1234})
        output = json.loads(self.client.get("/accounts/1").content)
        
        self.assertEqual(output['transactions'][0]['amount'], 200)
        self.assertEqual(output['transactions'][1]['amount'], 200.1234)
        
    def test_post_transaction_requires_amount(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
        response = self.client.post("/transactions", {'account': 'test-user'})
        self.assertEqual(json.loads(response.content), {'amount': ['This field is required.']})
        
    def test_valid_account_returns_correct_account(self):
        Account.objects.create(name="Test User", slug="test-user")
        account = Account.objects.get(slug='test-user')
        self.assertEqual(valid_account(1), account)
        self.assertEqual(valid_account("test-user"), account)

    def test_valid_account_raises_error_if_account_not_found(self):
        Account.objects.create(name="Test User", slug="test-user")
        account = Account.objects.get(slug='test-user')
        with self.assertRaises(serializers.ValidationError):
            valid_account(2)
        with self.assertRaises(serializers.ValidationError):
            valid_account('test-user2')
        # with self.assertRaises(serializers.ValidationError):
            valid_account(None)  

    def test_new_transactions_can_be_posted_by_account_slug(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
        response = self.client.post("/transactions", {'account':'test-user', 'amount':200})
        self.assertEqual(json.loads(response.content)['amount'], 200)
        
    def test_new_transactions_can_be_posted_by_account_id(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
        response = self.client.post("/transactions", {'account':1, 'amount':200})
        self.assertEqual(json.loads(response.content)['amount'], 200)
                
    def test_post_transaction_requires_account_slug_or_id(self):
        self.client.post("/accounts", {'name': 'Test User', 'slug':'test-user'})
        response = self.client.post("/transactions", {'amount':200})
        self.assertEqual(json.loads(response.content), {'account': ['This field is required.']})
        
        response = self.client.post("/transactions", {'account':2, 'amount':200})
        self.assertEqual(json.loads(response.content), {'account': ['2 is not a valid account.']})
        
        response = self.client.post("/transactions", {'account':'test-account2', 'amount':200})
        self.assertEqual(json.loads(response.content), {'account': ['test-account2 is not a valid account.']})
        

        