##Setup Instructions

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