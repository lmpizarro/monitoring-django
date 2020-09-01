import requests
import json

import utils as utils

def hello():
    utils.login()
    url_hello = utils.be_url.format("api/hello/")

    response = requests.get(url_hello, headers=utils.header)

    return response.json()


def temperature():
    url_temp = utils.be_url.format("api/temperature/")

    response = requests.get(url_temp, headers=utils.header)

    return response.json()


def bottlesByPerson():
    url_bott = utils.be_url.format("api/bottlesByPerson/")

    response = requests.get(url_bott, headers=utils.header)

    return (response.json())


def bottlesByMeeters(meeters=100):
    endpoint = f'api/get_bottles_meeters/{meeters}/'
    url_bott_meeters = utils.be_url.format(endpoint)

    response = requests.get(url_bott_meeters, headers=utils.header)

    return (response.json())

def bottlesByMeetersTemp(meeters=100, temp=30):
    endpoint = f'api/get_bottles_meeters_temp/'
    url_bott_meeters = utils.be_url.format(endpoint)

    data = {'temperature': temp,
            'meeters': 100}

    response = requests.post(url_bott_meeters,
                             data=json.dumps(data),
                             headers=utils.header)

    return (response.json())


if __name__ == '__main__':
    # main()
    utils.print_out(hello(), 'checkin')
    utils.print_out(temperature(), 'TEMPERATURA')
    utils.print_out(bottlesByPerson(), 'Bottles By Person')
    utils.print_out(bottlesByMeeters(), 'Bottles By Meeters')
    utils.print_out(bottlesByMeetersTemp(), 'Bottles By Meeters temperature')
