from django.db import models
from django.contrib.auth.models import User


class SensorValueType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class SensorType(models.Model):
    title = models.CharField(max_length=20)
    value_type = models.ForeignKey(SensorValueType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'


class Place(models.Model):
    room = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.room}'


class Sensor(models.Model):
    title = models.CharField(max_length=20)
    sensor_model = models.ForeignKey(SensorType, on_delete=models.SET_NULL, null=True)
    sensor_place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    sensor_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    info = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}: {self.sensor_model}'


class Monitoring(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.sensor} {self.value}'
