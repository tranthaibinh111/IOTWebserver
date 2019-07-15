from rest_framework import routers
from iot.apis import *

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet, base_name="sensors")
router.register(r'cron_handle', CronHandleViewSet, base_name="cron_handles")
router.register(r'humidity', HumidityViewSet, base_name="humidities")
router.register(r'temperature', TemperatureViewSet, base_name="temperatures")

urlpatterns += router.urls
