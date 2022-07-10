from rest_framework import serializers
from .models import Monitoring, Sensor, SensorType, SensorValueType


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = ('id', 'sensor', 'value', 'date')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'title', 'sensor_model', 'sensor_place', 'sensor_owner', 'info')


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('id', 'title', 'value_type')


class SensorValueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorValueType
        fields = ('id', 'title',)
