from django.test import TestCase, Client
from app.services import boxs_to_buy
from django.urls import reverse
import json
import requests
from datetime import datetime, timedelta, date
import pytz

from app.models import MeetUP, Meeter

# Create your tests here.
from birras.settings import TEMP_MIN, TEMP_MAX

# initialize client api
client = Client()


class ServiceTest(TestCase):
    be_url = "http://localhost:8080{}"
    header = {'Content-type': 'application/json'}

    def setUp(self):

        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        meetups = [
            {'name': 'monthly meeting 1',
             'meet_date': now + timedelta(hours=2),
             'place': 'place1',
             'description': 'nice monthly meeting'},
            {'name': 'monthly meeting 2',
             'meet_date': now + timedelta(days=30),
             'place': 'place1',
             'description': 'nice monthly meeting'},
            {'name': 'monthly meeting 3',
             'meet_date': now - timedelta(days=2),
             'place': 'place3',
             'description': 'nice monthly meeting'},
        ]

        for meetup in meetups:
            print('CREATING MEETUP')
            try:
                model = MeetUP.objects.create(**meetup)
                meetup['model'] = model
            except Exception as e:
                print(f'ERROR {e}')


        meeter = {'email': 'mario@gmail.com', 'name': 'mario gmail'}

        model_meeter: Meeter = Meeter.objects.create(**meeter)

        for meetup in meetups:
            meetup['model'].meeters.add(model_meeter)

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

    def test_get_meetups(self):
        self.login()

        url = self.be_url.format(reverse('getMeetUps'))

        response = requests.get(url, headers=self.header)

        self.assertEqual(len(response.json()), 2)

    def test_meetups_all(self):
        meetups = MeetUP.objects.all()

        self.assertEqual(meetups.count(), 3)

    def test_meetups_today(self):

        today = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=pytz.UTC)
        oneday = timedelta(days=1)
        endday = today + oneday

        meetups = MeetUP.objects.filter(meet_date__gt=today, meet_date__lt=endday)

        self.assertEqual(meetups.count(), 1)


    def test_meetups_today_endpoint(self):
        self.login()
        url = self.be_url.format(reverse('get_meetups_today'))

        response = requests.get(url, headers=self.header)

        self.assertEqual(response.json()['error'], False)
        assert 'date' in response.json()['meetups'][0]
        assert 'boxs_to_buy' in response.json()['meetups'][0]

    def test_meetup_details(self):
        meetup_qs = MeetUP.objects.all()

        meet_up_id = meetup_qs[0].id

        meetup: MeetUP = MeetUP.objects.get(pk=meet_up_id)

        assert meetup.name == 'monthly meeting 1'


    def test_meetup_details_endpoint(self):
        self.login()
        meetup_qs = MeetUP.objects.all()

        pk_meetup = meetup_qs[0].id

        url = self.be_url.format(reverse('get_meetup_details', kwargs={'pk': pk_meetup}))

        response = client.get(url)

        assert response.json()['meeters_count'] == 1
