# Revedy-Web


### Prerequisite:

    * Python 3.8.0+
   
       
1. Project setup, database setup and env set up

     * Pull from git repository 
     * Create virtual environment and apply to project
     * Run command for project dependency:
        ```
        $ pip install -r requirements.txt
        ```
     * Rename of .env(dev) to .env and update all variables values in .env
      
     * DB migrations:
        ```
        $ python manage.py migrate
        ```
2. Run server:
    ```
     $ python manage.py runserver
    ```
