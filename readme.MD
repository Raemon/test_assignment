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

(2) There are four modules:

1. Accounts -  