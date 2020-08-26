from django.conf import settings


import requests
import json


class Weather():

    def __init__(self):
        self.endpoint_weather = settings.WEATHER_API_URL.format(settings.WEATHER_PLACE, 
                                                                settings.WEATHER_APPID)
        
    def call_weather_api(self):                
        try:     
            response = requests.get(self.endpoint_weather)
            data = json.loads(response.text)
            data = data['main']
            data.pop('pressure', None)
            data.pop('humidity', None)
            data['error'] = False            
        except Exception as e:
            message = 'ERROR: {}'.format(e)
            data = {}
            data['error'] = True
            data['mesasge'] = message
   
        return data
         

