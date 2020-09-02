import requests
import json
from birras import settings

# implements
# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
class Weather:

    def __init__(self):
        self.endpoint_weather = settings.WEATHER_API_URL.format(settings.WEATHER_PLACE,
                                                                settings.WEATHER_APPID)

    @staticmethod
    def to_celsius(temp):
        return float('{:.2f}'.format(temp - 273.15))

    def get_temperature(self):
        data = self.call_weather_api()

        if not data['error']:
            return data['temp']
        else:
            return None

    def call_weather_api(self):
        try:
            response = requests.get(self.endpoint_weather)
            data = json.loads(response.text)
            data = data['main']
            data = {k: Weather.to_celsius(data[k]) for k in ['temp', 'temp_min', 'temp_max', 'feels_like']}
            data['error'] = False

        except Exception as e:
            message = 'ERROR: {}'.format(e)
            data = {}
            data['error'] = True
            data['mesasge'] = message

        return data
