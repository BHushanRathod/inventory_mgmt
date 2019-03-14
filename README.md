# Inventory Management 

A django application for inventory management

Source Code:
------------

`<https://github.com/BHushanRathod/inventory_mgmt.git>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/inventory_mgmt.git
   
Activate the Virtual Environment::

    source ~/path/to/ve/bin/activate

Install the Dependencies::

    pip install -r requirements.txt

Run Migrations::
    
    ./manage.py makemigrations
    ./manage.py migrate

Upload the seed data::

    ./manage.py loaddata InventoryStack.json
    
Create new superuser::
    
    ./manage.py createsuperuser

Run server::
    
    ./manage.py runserver <port>
    
* Steps to follow:
    * open postman, for list of inventory hit
    
            http://localhost:8000/inventory/list
            
    * For purchasing item hit, provide {'item':'item_id', 'quantity':'quantity'} with POST call
    
            http://localhost:8000/inventory/purchase
            
    * For getting purchase list, hit with GET call
    
            http://localhost:8000/inventory/purchase
            
    * To add or update an item hit, use /admin credentials as username:' bhushan' and pswd: 'qwerty@123'
    
            http://localhost:8000/admin/inventory_details/invertorystack/
