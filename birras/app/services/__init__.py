from django.conf import settings
import math
from datetime import datetime
import pytz
from app.models import MeetUP, Meeter
from datetime import date, timedelta
from app.services.weather import Weather
from birras import settings
from app.tasks import send_notification_delete_meetup
from app.services.emailsender import send_register_confirmation_email
from app.services.emailsender import send_register_delete_confirmatiom

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

        weather = Weather()

        begday = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=pytz.UTC)
        oneday = timedelta(days=1)
        endday = begday + oneday

        print(begday, endday)

        temperature = weather.get_temperature()

        if temperature == None:
            temperature = settings.TEMP_MIN

        try:
            meetups_qs = MeetUP.objects.filter(meet_date__gt=begday, meet_date__lt=endday)
            data = [{'date': meetup.meet_date,
                     'name': meetup.name,
                     'count_meeters': meetup.meeters.count(),
                     'boxs_to_buy': boxs_to_buy(temperature, meetup.meeters.count())} for meetup in meetups_qs]
            details['meetups'] = data
            details['error'] = False
        except Exception as e:
            print(f'ERROR {e}')


        return details

    def CreateMeetUP(self, data):
        try:
            model = MeetUP.objects.create(**data)
        except Exception as e:
            return None

        return model.id

    def DeleteMeetUp(self, pk):
        print('SERVICES', pk)
        try:
            model = MeetUP.objects.get(pk=pk)
            for meeter in model.meeters.all():
                send_notification_delete_meetup.delay(meeter.email, model.name)
            model.delete()

        except Exception as e:
            print(f'DeleteMeetUp ERROR {e}')
            return None

        return True

    def CreateMeeter(self, data):
        try:
            model = Meeter.objects.create(**data)
        except Exception as e:
            data['error'] = True
            data['message'] = str(e)
            return data

        # send requiere confirmation  via email
        send_register_confirmation_email(model.email)

        data['error'] = False
        data['meeter_id'] = model.id
        data['message'] = 'MEETER CREATED'

        return data

    def ConfirmCreateMeeter(self, email):

        data = {'error': True}
        try:
            model: Meeter = Meeter.objects.get(email=email)
            model.create_confirmation = True
            data['error'] = False
        except Exception as e:
            pass

        return data

    def SubscribeMeetUp(self, request_data):

        data = {'error': True}
        try:
            model_meeter: Meeter = Meeter.objects.get(email=request_data['email'])
        except Exception as e:
            message = 'NO_MEETER_IN_DB'
            data['message'] = message
            return data

        try:
            model_meetup: MeetUP = MeetUP.objects.get(pk=request_data['meetup_id'])
        except Exception as e:
            message = 'NO_MEETUP_IN_DB'
            data['message'] = message
            return data

        try:
            a = model_meetup.meeters.add(model_meeter)
            data['message'] = 'SUBSCRIPTION CREATED'
            data['error'] = False
            return data
        except Exception as e:
            message = 'MEETUP-MEETER_RELATION_NOT_CREATED'
            data['message'] = message
            return data


    def UnsubscribeMeetUp(self, request_data):
        print(request_data)

        data = {'error': True}
        try:
            model_meeter: Meeter = Meeter.objects.get(email=request_data['email'])
        except Exception as e:
            message = 'NO_MEETER_IN_DB'
            data['message'] = message
            return data

        try:
            model_meetup: MeetUP = MeetUP.objects.get(pk=request_data['meetup_id'])
        except Exception as e:
            message = 'NO_MEETUP_IN_DB'
            data['message'] = message
            return data

        try:
            a = model_meetup.meeters.remove(model_meeter)
            data['error'] = False
            data['message'] = 'UNSUBSCRIPTION SUCCESS'
            return data
        except Exception as e:
            message = 'MEETUP-MEETER_RELATION_NOT_CREATED'
            data['message'] = message
            return data

    def CheckinMeetUp(self, request_data):

        data = {'error': True}
        try:
            model_meeter: Meeter = Meeter.objects.get(email=request_data['email'])
        except Exception as e:
            message = 'NO_MEETER_IN_DB'
            data['message'] = message
            return data

        try:
            model_meetup: MeetUP = MeetUP.objects.get(pk=request_data['meetup_id'])
        except Exception as e:
            message = 'NO_MEETUP_IN_DB'
            data['message'] = message
            return data

        try:
            a = model_meetup.checkin.add(model_meeter)
            data['error'] = False
            return data
        except Exception as e:
            message = f'MEETUP-MEETER_RELATION_NOT_CREATED{e}'
            data['message'] = message
            return data


    def ConfirmDeleteMeeter(self, email):
        data = {'error': True, 'email': email}

        try:
            model = Meeter.objects.get(email=email)
            model_id = model.id
            model.delete()
            data['message'] = 'MEETER DELETED'
            data['meeter_id'] = model_id
            data['error'] = False
        except Exception as e:
            data['message'] = str(e)

        return data


    def DeleteMeeter(self, request_data):
        data = send_register_delete_confirmatiom(request_data['email'])

        return data
