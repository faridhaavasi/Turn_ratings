import time
from account.models import User
from django.db import models

# Create your models here.
class Hour(models.Model):
    hour = models.TimeField(time.thread_time_ns)
    def __str__(self):
        return f'{self.hour}'
class Mont(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Time(models.Model):
    yaer = models.IntegerField()
    mont = models.ForeignKey(Mont, on_delete=models.CASCADE, related_name='time')
    day = models.IntegerField(null=True, blank=True)

    hour = models.ForeignKey(Hour, on_delete=models.CASCADE, related_name='time')
    def __str__(self):
        return f'{self.yaer}-{self.mont}-{self.day}={self.hour}'
class Turn(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='turn')
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='turn')

    def __str__(self):
        return f'{self.number}-{self.time}'

