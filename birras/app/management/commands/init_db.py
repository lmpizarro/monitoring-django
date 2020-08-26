from django.core.management.base import BaseCommand
from app.models import Meeter, MeetUP

import datetime

class Command(BaseCommand):
    help = 'Init DB'

    meeters = [['mario@santader.com', 'mario'],
               ['rosa@alba.com', 'rosa'],
               ['ana@gmail.com', 'ana']]

    meetups = [
        ['anual meeting', datetime.datetime(2020, 10, 9, 18, 0, 0, 0), 'the place', 'nice anual meeting'],
        ['Reunion Barrio', datetime.datetime(2020, 11, 9, 21, 0, 0, 0), 'the other place', 'la reunion de barrio']
    ]

    def handle(self, *args, **options):

        try:
            Meeter.objects.all().delete()
            MeetUP.objects.all().delete()
        except Exception as e:
            print('ERROR DELETE DB')

        for m in self.meeters:
            email = m[0]
            name = m[1]

            try:
                model:Meeter = Meeter(email=email, name=name)
                model.save()
                m.append(model)
            except Exception as e:
                print(f'Error {e}')

        for m in self.meetups:
            try:
                model: MeetUP = MeetUP(name=m[0], meet_date=m[1], place=m[2], description=m[3])
                model.save()
                m.append(model)
            except Exception as e:
                print(f'Error {e}')

        # all meeters to meetup[0], meeter 0 y 2 meetup 1
        self.meetups[0][4].meeters.add(self.meeters[0][2])
        self.meetups[0][4].meeters.add(self.meeters[1][2])
        self.meetups[0][4].meeters.add(self.meeters[2][2])

        self.meetups[1][4].meeters.add(self.meeters[0][2])
        self.meetups[1][4].meeters.add(self.meeters[2][2])
