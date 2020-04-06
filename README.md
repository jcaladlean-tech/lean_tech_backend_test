# Lean Tech Backend Test

### Hello world (Project setup)

  *  Install [python 3,8](https://www.python.org/downloads/)
  *  Install requirements
  
        ```pip install -r requirements.txt```
  * Install project
  
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py groups
    python manage.py createsuperuser admin@admin.com
    ```
  * Run project
  
    ```python manage.py runserver```
  * Hello World Urls
     * [hola mundo txt](http://localhost:8000/holamundo/txt)
     * [hola mundo json](http://localhost:8000/holamundo/json)
  
### NoQSL and SQL
These two exercises are in NoSQL and SQL folders, the document schema and the SQL commands for postgreSQL

### Demo
This demo are created with the structure in the csv "Data", the urls for Get, Post, Put, Delete
  * [carrier](localhost:8000/demo/carrier)
  * [shipment](localhost:8000/demo/shipment)  
  * Filters
    * status
    * carrier name
    * origin state
    * origin city
    * destination state
    * destination city
    
### Authentication
In the first step we run a command (python manage.py groups), that command was to create admin and readonly roles
using the next endpoint to create user and get a token to authenticate

  * [create and list user](localhost:8000/user/user) 
    * It needs {username:"", email:"", password:""}
  * [login to get token](localhost:8000/auth/) 
    * It needs {username:"", password:""}
    * use the token in Authorization header in this way ==>      token {token}