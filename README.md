# vendor-management-system

Installation

    Running locally
        Clone the repository
        Change directory to elevator
        Create a virtual environment        
        Activate the virtual environment and install the requirements
        Install Required Libraries
        Run the server

     - git clone
     - cd elevator
     - virtualenv venv
     - source venv/bin/activate
     - pip install django==4.2.1
     - pip install djangorestframework==3.14.0
     - pip install psycopg2-binary==2.9.6
     - pip install pytz==2023.3
     - pip install sqlparse==0.4.4
     - python manage.py runserver or python3 manage.py runserver


File Structure  
```
  ├── README.md
  |── vendor
  |  ├── vendor_system
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  |  ├── main
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   ├── models.py
  │   ├── serializer.py
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── manage.py
```


Usage

    Create new vendor
        Endpoint: /api/vendors/
        Method : POST
        Request body:

    {
        "name": "your name",
        "contact": "youremail@gmail.com",
        "address" : "new delhi"
    }

Get all Vendors
        Endpoint: /api/vendors/
        Method : Get   

Get a vendors info

    Endpoint: api/vendors/<int:pk>
    Method: GET

Update vendor details

    Endpoint: api/vendors/<int:pk>/
    Method : PATCH
```
Delete a vendor

    Endpoint: api/Vendors/<int:pk>/
    Method : Delete

Create  Order
        Endpoint: /api/purchase_orders/
        Method : POST
        Request body:

    {
        "vendor": "vendor_instance",
        "delivery_date": "yyyy-mm-dd",
        "items" : "Json Object",
        "quanity": total quantity,
        "status":"pending",      
    }

Get all orders
        Endpoint: api/purchase_orders/
        Method : Get   

Get a order detail

    Endpoint: api/purchase_orders/<int:pk>
    Method: GET

Update order details

    Endpoint: api/purchase_orders/<int:pk>/
    Method : PATCH

    you can give quality rating   
```
Delete a order

    Endpoint: api/purchase_orders/<int:pk>/
    Method : Delete

Acknowledge the order

    Endpoint: api/purchase_orders/<int:pk>/acknowledge/
    Method : Patch
    
Get performance of vendor

    Endpoint:api/vendors/<int:pk>/performance/
    Method : Get

    


    
