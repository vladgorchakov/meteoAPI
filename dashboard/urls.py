from django.urls import path
from .views import DashboardListApi, SensorListApi, SensorUpdateApi, SensorTypeListApi, SensorTypeUpdateApi, \
    SensorValueTypeListApi, SensorValueTypeUpdateApi, PlaceList, PlaceUpdate


urlpatterns = [
    path('', DashboardListApi.as_view()),
    path('sensors/', SensorListApi.as_view()),
    path('sensors/<int:pk>', SensorUpdateApi.as_view()),
    path('sensors/type/', SensorTypeListApi.as_view()),
    path('sensors/type/<int:pk>', SensorTypeUpdateApi.as_view()),
    path('sensors/valuetype/', SensorValueTypeListApi.as_view()),
    path('sensors/valuetype/<int:pk>', SensorValueTypeUpdateApi.as_view()),
    path('sensors/place/', PlaceList.as_view()),
    path('sensors/place/<int:pk>/', PlaceUpdate.as_view()),
]
