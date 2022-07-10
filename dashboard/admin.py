from django.contrib import admin
from .models import *

admin.site.register(Sensor)
admin.site.register(SensorType)
admin.site.register(SensorValueType)
admin.site.register(Place)
admin.site.register(Monitoring)
