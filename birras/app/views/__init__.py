# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.services import TemperatureLogic
from app.services.weather import Weather


class HelloBeerService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, I am the Beer Service!'}
        return Response(content)


class GetWeatherTemperature(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        WS = Weather()

        temperature = WS.call_weather_api()

        return Response(temperature)


class GetBottlesByPerson(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        WS = Weather()

        temperature = WS.call_weather_api()

        data = {}
        if temperature['error'] == False:

            temperature = temperature['temp']
            TL = TemperatureLogic()
            bottle_by_person = TL.discriminator(temperature)

            data['bottle_by_person'] = bottle_by_person
            data['error'] = False
        else:
            data['error'] = True

        return Response(data)