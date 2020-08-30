# Readme project test birras

size box 6

20 < T < 24 1 bottle_by_person
T < 20 0.75 bottle_by_persom
T > 24  2 plus bottle_by_person

## ALERT: the requirement is ambiguous

as an admin I want to know the amount of beer to buy

as an admin and as a user I want to know the weather temperature

as an admin and as a user I want to receive meetups notifications

as an admin I want to organize a meetup and invite peoples

as a user I want to register i an meetup

as a user I want to check in a meetup (to register that I was there)


## Take into accouny
- swagger
- Cache, Retry, Circuit Breaker, maturity level, I18N, reactive
- Security
- Front Responsive/pwa
- Test UI
- Automatic Testing 

### Apis weather:

[rapidapi] (https://rapidapi.com)

- open-weather-map
- weather
- AccuWeather
- dark-sky

## Run the project


### Create the database

```
$ sudo su - postgres
```
```
$ psql
```

```
CREATE DATABASE birras;
CREATE USER birras WITH PASSWORD 'birras';
ALTER ROLE birras SET client_encoding TO 'utf8';
ALTER ROLE birras SET default_transaction_isolation TO 'read committed';
ALTER ROLE birras SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE birras TO birras;
ALTER USER birras CREATE DB;
\q

```


Clone the repo

``` 
$ git clone https://git-rba.hackerrank.com/git/a54e03ce-9448-4e4b-9c75-b1af5a0175e8
$ cd a54e03ce-9448-4e4b-9c75-b1af5a0175e8
```

Create de python local virtual evironment
```
$ python3 -m venv venv
```

Activate de Python virtual evironment
```
$ source venv/bin/activate
```

Install the project requirements

```
$ pip install -r birras/requirements.txt
```

Apply the migrations to the sql db

```
$ cd birras
$ python manage.py migrate
```

Run the django project

```
$ python manage.py runserver 0.0.0.0:8080
```

In another terminal, run the celery worker and scheduler

```
$ cd a54e03ce-9448-4e4b-9c75-b1af5a0175e8/birras
$ celery worker -A app -l info -B
```

Open the application
```
$ firefox http://localhost:8080/admin/
``` 


## Docker

Build de project

```
$ docker-compose build
```

Run the project

```
$ docker-compose up
```

Stop the project

```
$ docker-compose down -v remove-orphans
```


clean up unused images
```
$ docker image prune
```

remove all images which are not used by existing containers
```
$ docker image prune -a
```


Delete all containers using the following command:
```
$ docker rm -f $(docker ps -a -q)
```

Delete all volumes using the following command:
```
$ docker volume rm $(docker volume ls -q)

```

## TODO
[circuitbreaker](https://pypi.org/project/circuitbreaker/)



## Referencias

[django](https://www.djangoproject.com/)
[celeryproject](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
[django-rest-framework](https://www.django-rest-framework.org/tutorial/quickstart/)
[django-rest-framework-jwt](https://jpadilla.github.io/django-rest-framework-jwt/)
[swagger generator](https://drf-yasg.readthedocs.io/en/stable/readme.html)
[flower](https://flower.readthedocs.io/en/latest/)
[grappelli](https://grappelliproject.com/)
[whitenoise](http://whitenoise.evans.io/en/stable/)
[grafana](https://grafana.com/)
[prometheus](https://prometheus.io/docs/introduction/overview/)
[django-prometheus](https://github.com/korfuri/django-prometheus)
[Docker](https://www.docker.com/)
[how-to-use-jwt-authentication-with-django-rest-framework](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)
[monitoring](https://www.sipios.com/blog-tech/monitoring)
[django prometheus docker compose](https://github.com/vegasbrianc/prometheus)
[Docker_Prometheus_Grafana](https://www.bogotobogo.com/DevOps/Docker/Docker_Prometheus_Grafana.php)
[pruning](https://docs.docker.com/config/pruning/)
