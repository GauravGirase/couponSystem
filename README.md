# COUPON SYSYTEM


### Prerequisite:

    * Python 3.8.0+
   
       
1. Project setup, database setup and env set up

     * Pull from git repository 
     * Create virtual environment and apply to project
     * Run command for project dependency:
        ```
        $ pip install -r requirements.txt
        ```
      
     * DB migrations:
        ```
        $ python manage.py migrate
        ```
2. Run server:
    ```
     $ python manage.py runserver
    ```
3. API endpoints:
    * list all the coupons available in database:
    
    ```
         $ http://127.0.0.1:8000/api/v1

    Example:

    [
        {   
            "id": 1,
            "code": "123",
            "discount": 20,
            "active": true
        },
        {   
            "id": 2,
            "code": "CODEx1",
            "discount": 25,
            "active": true
        },
        {
            "id": 3,
            "code": "CODE-XYZ",
            "discount": 40,
            "active": true
        },
        {
            "id": 4,
            "code": "X89",
            "discount": 70,
            "active": true
        }
    ]
    ```
    
    * To get details or delete particular coupons available in database:

    ```
     $ http://127.0.0.1:8000/api/v1/coupon/<id>

    ```
    * To redeem the coupon , the user needs to pass coupon code as query parameter:

    ```
     $ http://127.0.0.1:8000/api/v1/redeem/<coupon_code>
    ```