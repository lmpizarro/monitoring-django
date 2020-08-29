from django.core.management.base import BaseCommand
from app.models import Meeter, MeetUP

from django.utils import timezone
import pytz

from datetime import datetime
from datetime import timedelta

class Command(BaseCommand):
    help = 'Init DB'

    meeters = [
               ['mario@santader.com', 'mario'],
               ['rosa@alba.com', 'rosa'],
               ['ana@gmail.com', 'ana'],
               ['rosa2@alba.com', 'rosa2'],
               ['rosa3@alba.com', 'rosa3'],
               ['rosa4@alba.com', 'rosa4'],
               ['rosa5@alba.com', 'rosa5'],
               ['rosa6@alba.com', 'rosa6'],
               ['rosa7@alba.com', 'rosa7'],
               ['rosa8@alba.com', 'rosa8'],
               ['rosa9@alba.com', 'rosa9'],
               ['rosa10@alba.com', 'rosa10'],
               ['rosa11@alba.com', 'rosa11'],
               ['rosa12@alba.com', 'rosa12'],
               ['rosa13@alba.com', 'rosa13'],
               ['rosa14@alba.com', 'rosa14'],
               ['rosa15@alba.com', 'rosa15'],
              ]

    meetups = [
        ['anual meeting', datetime(2020, 10, 9, 18, 0, 0, 0).replace(tzinfo=pytz.utc),
         'the place', 'nice anual meeting'],
        ['Reunion Barrio', datetime(2020, 11, 9, 21, 0, 0, 0).replace(tzinfo=pytz.utc),
         'the other place', 'la reunion de barrio'],
        ['python for all', datetime.utcnow().replace(tzinfo=pytz.utc) + timedelta(hours=12),
         'the python place', 'python is nice']
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

        for i in range(3, 17):
            self.meetups[2][4].meeters.add(self.meeters[i][2])



