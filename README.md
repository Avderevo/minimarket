# Minimarket
A simple store with a category page of goods, a page of the list of goods and a page of one product.

# Installation

For installation it is recommended to use a virtual environment.


Create a new directory and clone the application.

```
$ git clone https://github.com/Avderevo/minimarket
```

# Requipments

### For development:

```
$ pip install -r requipments/development.txt
```
### configuration of environment variables:

```
export APP_SETTINGS="config.DevelopmentConfig"
```

### if the database is different from sqlite:


Need to be replaced with their database access requisites: DBUSERNAME, DBPASSWORD and DBNAME 

```
export DATABASE_URL='postgresql://DBUSERNAME:DBPASSWORD@localhost/DBNAME'
```

# Local run

```
$ python manage.py runserver
```

### basic commands:

```
 $ python manage.py db init
 $ python manage.py db migrate
 $ python manage.py db upgrade
 $ python manage.py db shell
 $ python manage.py runserver
```
# Sample application pages

