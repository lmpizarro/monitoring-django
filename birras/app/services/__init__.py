from django.conf import settings
import math
from datetime import datetime
import pytz
from app.models import MeetUP
from datetime import date, timedelta


class TemperatureLogic:

    def __init__(self,
                 lowerLevel=settings.TEMP_MIN,
                 upperLevel=settings.TEMP_MAX):
        self.low = lowerLevel
        self.max = upperLevel

    def discriminator(self, temp):
        if temp <= self.low:
            return 0.75
        elif temp > self.max:
            return 2.0
        else:
            return 1.0

def boxs_to_buy(temp, meeters):
    tl = TemperatureLogic()

    bot_per_meet = tl.discriminator(temp)

    print(bot_per_meet)
    bottles = math.floor(meeters * bot_per_meet)

    while bottles % 6:
        bottles += 1
    return bottles / 6


class MeetUPInterface:

    def getActiveMeetUps(self):

        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        meetup_qs = MeetUP.objects.filter(meet_date__gte=now)

        meetups = []
        for meetup in meetup_qs:
            meetups.append({'meetup_id': meetup.id, 'name': meetup.name, 'datetime': meetup.meet_date})

        return meetups

    def getMeetUpsDetails(self, pk):
        details = {}

        try:
            meetup_model: MeetUP = MeetUP.objects.get(pk=pk)
            meeters = meetup_model.meeters
            count = meeters.count()
            details['error'] = False
            details['meeters_count'] = count
            details['name'] = meetup_model.name
            details['meet_date'] = meetup_model.meet_date
        except Exception as e:
            details['error'] = True

        return details

    def getMeetUpsToday(self):
        details = {'error': True}

        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        today = date.today() + timedelta(days=1)
        midnight = datetime.combine(today, datetime.min.time())
        print(now, midnight)
        try:
            meetup_qs = MeetUP.objects.filter(meet_date__gte=now, meet_date__lt=midnight)
            data = [{'date': meetup.meet_date,
                     'name': meetup.name,
                     'count_meeters': meetup.meeters.count()} for meetup in meetup_qs]
            details['meetups'] = data
            details['error'] = False
        except Exception as e:
            print(f'ERROR {e}')


        return details
