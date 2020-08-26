from django.db import models

# Create your models here.

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

    def __str__(self):
        return f'{self.name} {self.meet_date}'



