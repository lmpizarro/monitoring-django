from django.contrib import admin

from birras import settings

# Register your models here.

from app.models import MeetUP, Meeter, CurrentTemperature
from app.services import boxs_to_buy

@admin.register(MeetUP)
class MeetUpAdmin(admin.ModelAdmin):
    list_display = ['name', 'meet_date', 'place', 'get_meeters', 'min_bottles', 'min_boxs']
    list_filter = ['meet_date']
    
    def get_meeters(self, obj):
        return obj.meeters.all().count()
        
    def min_bottles(self, obj):
         return settings.BOTTLES_MIN * self.get_meeters(obj)

    def min_boxs(self, obj):
        return boxs_to_buy(settings.TEMP_MIN, self.get_meeters(obj))

@admin.register(Meeter)
class MeeterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'get_meetups']
    
    def get_meetups(self, obj):
        return obj.meetup_set.all().count()


@admin.register(CurrentTemperature)
class CurrentTemperatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'temp', 'temp_min', 'temp_max', 'feels_like']

