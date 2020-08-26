from django.shortcuts import render
from django.conf import settings

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


import requests
import json


class HelloBeerService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, I am the Beer Service!'}
        return Response(content)
        

class GetWeatherTemperature(APIView):

    # http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=80094b733f66d8d7096912d870c78fd5
 

    def call_weather_api(self):
                 
        endpoint_weather = settings.WEATHER_API_URL.format(settings.WEATHER_PLACE, settings.WEATHER_APPID)
   
        try:     
            response = requests.get(endpoint_weather)
            data = json.loads(response.text)
            data = data['main']
            data.pop('pressure', None)
            data.pop('humidity', None)
            data['error'] = False            
        except Exception as e:
            print('ERROR: {}'.format(e))
            data['error'] = True
   
        return data
        
    def get(self, request):
        # call weather api
        
        temperature = self.call_weather_api()
        
        return Response(temperature)

    
