# Leonardo's Django Coding Test #
Coding test to evaluate skills using Python and Django Web Framework.

## Getting Started ##
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Running with Docker ###

**Prerequisites**

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

**Installing**

Get the source code:

```
git clone https://github.com/leomfelicissimo/employees_test.git
```

Enter the app folder:

```
$ cd employees_test/app
```

Use docker-compose to run the full stack:

```
$ docker-compose up -d
```

Execute _docker ps_ for assert the up of containers

```
$ docker ps
```

It must bring the following containers on list:
```
empsrv: Reverse proxy (nginx) for the app
empapp: Django Web Application 
empdb: Postgres Database
```

Create the superuser for Django Admin access, following the steps to set a email and password:
```
$ docker exec -it empapp python manage.py createsuperuser --username <username>
```

For access the Django Admin, you can access: http://localhost:8000/admin
For the api interface. you can access: http://localhost:8000/employee

### Running with Django CLI ### 

**Prerequisites**

- [Python 3.7.3](https://docs.docker.com/install/)

**Installing**

Get the source code:

```
git clone https://github.com/leomfelicissimo/employees_test.git
```

Enter the folder:

```
$ cd employees_test
```

Use venv for create an environment for the app:

*If you have an older version of python you must use python3 bin*

```
$ python -m venv venv
```

Execute the venv:

```
$ source venv/bin/activate
```

If it's ok, you must be seeing a __(venv)__ before your bash:
```
(venv) $ 
```

Go to the app folder:
```
(venv) $ cd app
```

Install the requirements with pip:
```
(venv) $ pip install -r requirements.txt
```

Create the super user for Django Admin:
```
(venv) $ python manage.py createsuperuser --username <username>
```

Execute the server:
```
(venv) $ python manage.py runserver
```

Now, you can navigate to: http://localhost:8000/admin

## Running the tests ##

### Running with Docker ###
From the project folder (__app__ of employees_test), execute:
```
$ docker exec empapp python manage.py test
```

### Running with Django CLI ###
From the project folder (__app__ of employees_test), execute:
```
$ python manage.py test
```

### CircleCI Link ###
The test have a pipeline created for build and test, you can access it [here](https://circleci.com/gh/leomfelicissimo/employees_test).

## Built With ##
- [Django Web Framework](https://www.djangoproject.com/): The Web framework for perfectionists with deadlines
- [Django REST Framework](https://www.django-rest-framework.org/): Django REST framework is a powerful and flexible toolkit for building Web APIs
- [Docker/Compose](https://www.docker.com): Build, Ship, and Run Any App, Anywhere.
- [Postgres](https://www.postgresql.org/download/): PostgreSQL is a powerful, open source object-relational database system
- [CircleCI](https://circleci.com/): CircleCI integrates with GitHub, GitHub Enterprise, and Bitbucket. Every time you commit code, CircleCI creates a build. Automate your pipeline from commit to deploy.

## Author ##
- Leonardo Felicissimo

## Remarks ##
There are a lot of scenarios not tested, many validations and others that would improve the quality, security by Token or using an API Gateway, cache with Redis, logging with ELK Stack and other good practices not applied, but I think that is not so relevant for the coding testing purpose. 

My interest was depĺoy the solution with Kubernetes, but we don't have so much time for that now.

Thank you!
