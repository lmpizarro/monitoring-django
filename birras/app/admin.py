from django.contrib import admin
from django.conf import settings

# Register your models here.

from app.models import MeetUP, Meeter, CurrentTemperature


@admin.register(MeetUP)
class MeetUpAdmin(admin.ModelAdmin):
    list_display = ['name', 'meet_date', 'place', 'get_meeters', 'min_bottles']
    
    def get_meeters(self, obj):
        return obj.meeters.all().count()
        
    def min_bottles(self, obj):
         return settings.TEMP_WEATHER_MIN * self.get_meeters(obj)

@admin.register(Meeter)
class MeeterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'get_meetups']
    
    def get_meetups(self, obj):
        return obj.meetup_set.all().count()


@admin.register(CurrentTemperature)
class CurrentTemperatureAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'temp', 'temp_max']

