# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.services import TemperatureLogic
from app.services.weather import Weather

weather_service = Weather()
temperature_logic = TemperatureLogic()


class HelloBeerService(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {'error': False,
                'message': 'Hello, I am the Beer Service!',
                'endpoint': 'hello_beer'}

        return Response(data)


class GetWeatherTemperature(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        temperature = weather_service.call_weather_api()
        temperature['endpoint'] = 'temperature'
        return Response(temperature)


class GetBottlesByPerson(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        temperature = weather_service.call_weather_api()

        data = {}
        if temperature['error'] == False:

            temperature = temperature['temp']
            bottle_by_person = temperature_logic.discriminator(temperature)

            data['bottle_by_person'] = bottle_by_person
            data['error'] = False
        else:
            data['error'] = True

        data['endpoint'] = 'bottles_by_person'
        return Response(data)


class GetBottlesMeeters(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request, meeters, format=None):

        temperature = weather_service.call_weather_api()

        data = {'endpoint': 'bottles_meeters'}

        if temperature['error'] == False:

            temperature = temperature['temp']
            bottle_by_person = temperature_logic.discriminator(temperature)

            data['bottles_to_buy'] = bottle_by_person * meeters
            data['error'] = False
        else:
            data['error'] = True

        return Response(data)


class GetBottlesMeetersTemp(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = {'endpoint': 'get_bottles_meeters_temp'}
        print(request.data)
        bottle_by_person = temperature_logic.discriminator(request.data['temperature'])
        bottle_to_buy = bottle_by_person * request.data['meeters']
        data['bottles_to_buy'] = bottle_to_buy

        return Response(data)
