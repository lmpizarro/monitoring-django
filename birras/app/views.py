from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloBeerService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, I am the Beer Service!'}
        return Response(content)
        

class GetWeatherTemperature(APIView):

    def call_weather_api():
        return 24
        
    def get(self, request):
        # call weather api
        
        temperature = call_weather_api()
        
        content = {'temperature': f'{temperature}'}
        return Response(content)

    
