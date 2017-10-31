from django.db import models
from django.contrib.auth.models import User


class Beacon(models.Model):
    uuid = models.UUIDField()
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    z = models.IntegerField(default=0)

    def __str__(self):
        return str(self.uuid)

class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=32)
    beacon_total_number = models.IntegerField(default=0)

    def __str__(self):
        return '{}가 {}에 보낸 신호'.format(self.user, self.created_at)

class Signal(models.Model):
    beacon = models.ForeignKey(Beacon)
    time = models.ForeignKey(Time, related_name="signals")
    rssi = models.IntegerField(default=0)


