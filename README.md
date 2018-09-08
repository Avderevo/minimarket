[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Avderevo/minimarket/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Avderevo/minimarket/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/Avderevo/minimarket/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Avderevo/minimarket/build-status/master)


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

### Page of one product:

<hr>

![alt text](https://github.com/Avderevo/minimarket/blob/master/screenshots/Screenshot%20from%202018-08-25%2017.13.23.png)

<hr>

### Product List Page:

<hr>

![alt text](https://github.com/Avderevo/minimarket/blob/master/screenshots/Screenshot%20from%202018-08-25%2017.14.46.png)

