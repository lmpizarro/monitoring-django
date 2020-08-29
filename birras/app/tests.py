from django.test import TestCase, Client
from app.services import boxs_to_buy
from django.urls import reverse
import json
import requests

# Create your tests here.
from birras.settings import TEMP_MIN, TEMP_MAX

# initialize client api
client = Client()

class ServiceTest(TestCase):

    be_url = "http://localhost:8080{}"
    header = {'Content-type': 'application/json'}

    def setup(self):
        pass

    def set_header(self, authorization):
        self.header['Authorization'] = f'Bearer {authorization}'

    def login(self, user='admin', password='admin'):
        url = self.be_url.format(reverse('token_obtain_pair'))

        payload = {'username': user, 'password': password}
        headers = {}

        response = requests.post(url,
                               headers=headers,
                               data=payload)

        self.set_header(response.json()['access'])

    def test_login(self, user='admin', password='admin1'):
        url = self.be_url.format(reverse('token_obtain_pair'))

        payload = {'username': user, 'password': password}
        headers = {}

        response = requests.post(url,
                               headers=headers,
                               data=payload)


        assert 'detail' in response.json()
        assert response.json()['detail'].endswith('credentials')


    def test_boxs_to_buy(self):
        
        boxs = boxs_to_buy(24, 100)
        
        assert boxs == 17

    def test_hello(self):
        self.login()

        url = self.be_url.format(reverse('hellobeer'))
        response = requests.get(url, headers=self.header)

        assert 'message' in response.json()
        assert response.json()['message'].startswith('Hello')

    def test_temperature(self):
        self.login()

        url = self.be_url.format(reverse('gettemperature'))
        response = requests.get(url, headers=self.header)

        keys = ['temp', 'temp_min', 'temp_max', 'feels_like']
        data = response.json()

        assert not data['error']

    def test_bottles_by_person(self):
        self.login()

        url = self.be_url.format(reverse('bottleByPerson'))

        response = requests.get(url, headers=self.header)

        assert 'bottle_by_person' in response.json()
        assert not response.json()['error']

