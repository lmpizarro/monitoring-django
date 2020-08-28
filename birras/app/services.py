from django.conf import settings
import requests
import json

# implements
# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=80094b733f66d8d7096912d870c78fd5
class Weather():

    def __init__(self):
        self.endpoint_weather = settings.WEATHER_API_URL.format(settings.WEATHER_PLACE, 
                                                                settings.WEATHER_APPID)
        
    @staticmethod
    def to_celsius(temp):
        return float('{:.2f}'.format(temp - 273.15))
        
    def call_weather_api(self):                
        try:     
            response = requests.get(self.endpoint_weather)
            data = json.loads(response.text)
            data = data['main']            
            data = {k:Weather.to_celsius(data[k]) for k in ['temp', 'temp_min', 'temp_max', 'feels_like']}
            data['error'] = False
 
        except Exception as e:
            message = 'ERROR: {}'.format(e)
            data = {}
            data['error'] = True
            data['mesasge'] = message
   
        return data
         

class TemperatureLogic():

    def __init__(self, lowerLevel=settings.TEMP_MIN, upperLevel=settings.TEMP_MAX):
       self.low = lowerLevel
       self.max = upperLevel
       
    def discriminator(self, temp):
       if temp < self.low:
           return 0.75
       elif temp > self.max:
           return 2.0
       else:
           return 1.0
           
def boxs_to_buy(temp, meeters):
    tl = TemperatureLogic()
    
    bot_per_meet = tl.discriminator(temp)
    
    bottles = int(meeters * bot_per_meet)
    
    while bottles % 6:
        bottles +=1
    return bottles / 6

