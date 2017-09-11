Setup Instructions
------------------

1. Clone the Git Repo
2. Create a Virtual Python3 Environment
3. Activate the Virtual Environment
4. Install the project requirements
5. Run the latest database migrations to setup your database
6. Run the server

```
git clone https://github.com/Raemon/test_assignment.git
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Once the server is running, you can create new accounts:

```
curl -H 'Content-Type:application/json' -XPOST "http://localhost:8000/accounts" -d '{ "name":"Example Account", "slug":"example-account"}'
```

And new transactions:


```
curl -H 'Content-Type:application/json' -XPOST "http://localhost:8000/transactions" -d '{ "account":"example-account", "amount":200}'
```

Notes on some design choices:

(1). I have a default-setup I typically use for APIs, using Django and the corresponding Django-Rest-Framework. It includes some database-model mixins for a created/updated timestamp, and a name/slug identifier (with names allowing any characters, slugs disallowing special characters that'd make it harder to use in URLs and the like)

I tweaked the API Serializer to use "timestamp" to show the Transaction's "created" DateTime field, so that it still matched the specifications. Accounts currently require both a name and a slug.

Since I was working in Django, which is a bit opinionated, I chose to have Ledger entries stored as a separate Entry database model instead of, say, a list of numbers in the Ledger, but if I were using other frameworks may have had a different approach.

(2) Overall architecture - there are four modules, each with accompanying unit tests.

1. Accounts - Models for the Accounts, Journals, Ledgers, Transactions and Entries, as well as Manager classes that handle the initialization of new accounts and transactions.

2. API - Serializers and Views using the Django-Rest-Framework for accounts and transactions

3. Capitalone - the core project folder, which includes the health API endpoint and the basic settings, url routing, etc.

4. Common - Mixins I use to provide the timestamp and name/slug functionality.

(3) Testing Approach

I made sure that each of the project requirements were covered by a test, and that the API calls specified by the assignment had enough tests that if we were to refactor the entire underlying architecture we'd be able to make sure the thing still worked.

Beyond that, I try to have a modular approach, breaking tasks into small functions, testing each function for its unique logic and using mocks to make sure that it calls the sub-functions correctly. (I ran into an instance where this *didn't* work while testing the transaction serializer, due to something about how Django handles its fields. I spent 30-45 minutes trying to debug that and then decided it was more important to get the assignment in promply, although I'll be continuing to look into that)

