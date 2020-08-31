from django.db import models
# Create your models here.
from django.utils import timezone


class Meeter(models.Model):
    email = models.EmailField(null=False, unique=True)
    name = models.CharField('Meeter Name', max_length=200, null=True)

    def __str__(self):
        return self.email


class MeetUP(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    meet_date = models.DateTimeField('meet up date', null=True)
    place = models.TextField('The Place', max_length=512, null=True)
    description = models.TextField('Brief', max_length=512, null=True)
    meeters = models.ManyToManyField(Meeter, blank=True)
    checkin = models.ManyToManyField(Meeter, related_name='meeters_checkin')

    def __str__(self):
        return f'{self.name} {self.meet_date}'




class CurrentTemperature(models.Model):
      date_time = models.DateTimeField('time', default=timezone.now, null=True)
      temp = models.FloatField('Current Temperature')
      temp_min = models.FloatField('Min Temperature')
      temp_max = models.FloatField('Max Temperature')
      feels_like = models.FloatField('Feels Like')

      def __str__(self):
          return str(self.temp)




