from django.db import models

# Create your models here.

class MeetUP(models.Model):
    name = models.CharField(max_length=200, null=False)
    meet_date = models.DateTimeField('meet up date', null=True)
    place = models.TextField('The Place', max_length=512, null=True)
    description = models.TextField('Brief', max_length=512, null=True)

    def __str__(self):
        return f'{self.name} {self.meet_date}'



