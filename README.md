# test birras

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


- swagger
- Cache, Retrey, Circuit Breaker, maturity level, I18N, reactive
- Security
- Front Responsive/pwa
- Test UI
- Automatic Testing 

Apis weather:

[rapidapi] (https://rapidapi.com)

- open-weather-map
- weather
- AccuWeather
- dark-sky

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## TODO
[circuitbreaker](https://pypi.org/project/circuitbreaker/)

## Docker


[pruning](https://docs.docker.com/config/pruning/)

clean up unused images
```
docker image prune
```

remove all images which are not used by existing containers
```
docker image prune -a
```



Delete all containers using the following command:
```
docker rm -f $(docker ps -a -q)
```

Delete all volumes using the following command:
```
docker volume rm $(docker volume ls -q)

```
