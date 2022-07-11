from rest_framework import generics
from .serializers import DashboardSerializer, SensorSerializer, SensorTypeSerializer, \
    SensorValueTypeSerializer, PlaceSerializer
from .models import Monitoring, Sensor, SensorType, SensorValueType, Place, User


class DashboardListApi(generics.ListCreateAPIView):
    serializer_class = DashboardSerializer
    queryset = Monitoring.objects.all().order_by('-date')


class SensorListApi(generics.ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorTypeListApi(generics.ListCreateAPIView):
    serializer_class = SensorTypeSerializer
    queryset = SensorType.objects.all()


class SensorTypeUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorTypeSerializer
    queryset = SensorType.objects.all()


class SensorValueTypeListApi(generics.ListCreateAPIView):
    serializer_class = SensorValueTypeSerializer
    queryset = SensorValueType.objects.all()


class SensorValueTypeUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorValueTypeSerializer
    queryset = SensorValueType.objects.all()


class PlaceList(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class PlaceUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
