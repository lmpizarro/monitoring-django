from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from app.services import Weather

class HelloBeerService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, I am the Beer Service!'}
        return Response(content)


       

class GetWeatherTemperature(APIView):

    # http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=80094b733f66d8d7096912d870c78fd5
 

        
    def get(self, request):
        # call weather api
        
        WS = Weather()
        
        temperature = WS.call_weather_api()
        
        return Response(temperature)

    
