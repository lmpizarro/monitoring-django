from django.core.management.base import BaseCommand
from app.models import Meeter, MeetUP

import datetime

class Command(BaseCommand):
    help = 'Init DB'

    meeters = [('mario@santader.com', 'mario'),
               ('rosa@alba.com', 'rosa'),
               ('ana@gmail.com', 'ana')]

    meetups =[
        ('anual meeting', datetime.datetime(2020, 10, 9, 18, 0, 0, 0), 'the place', 'nice anual meeting'),
        ('Reunion Barrio', datetime.datetime(2020, 11, 9, 21, 0, 0, 0), 'the other place', 'la reunion de barrio')
    ]

    def handle(self, *args, **options):
        for m in self.meeters:
            email = m[0]
            name = m[1]

            try:
                model:Meeter = Meeter(email=email, name=name)
                model.save()
            except Exception as e:
                print(f'Error {e}')

        for m in self.meetups:
            try:
                model: MeetUP = MeetUP(name=m[0], meet_date=m[1], place=m[2], description=m[3])
                model.save()
            except Exception as e:
                print(f'Error {e}')

