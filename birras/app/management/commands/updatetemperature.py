from django.core.management.base import BaseCommand
from app.models import CurrentTemperature
from app.services import Weather
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            qs = CurrentTemperature.objects.all()
            for e in qs[9:]:
               e.delete()
        except Exception as e:
            print('ERROR DELETE DB')


        weather = Weather()

        data = weather.call_weather_api()

        if data['error'] == False:
            del data['error']
            model = CurrentTemperature(**data)

            model.save()
