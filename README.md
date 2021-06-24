# couponSystem
A sample project showing how to build a scalable, maintainable, API with DjangoREST


Running the app
Preferably, first create a virtualenv and activate it, perhaps with the following command:

virtualenv venv
venv\Scripts\Activate
Next, run

pip install -r requirements.txt
to get the dependencies.

Next, initialize the database

python manage.py migrate
Type "Y" to accept the message (which is just there to prevent you accidentally deleting things -- it's just a local SQLite database)

Finally run the app with

python manage.py runserver
