from django.contrib import admin
from iot.models import *
from .device_type import DeviceTypeAdmin
from .sensor import SensorAdmin
from .cron_handle import CronHandleAdmin
from .humidity import HumidityAdmin
from .temperature import TemperatureAdmin


admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(CronHandle, CronHandleAdmin)
admin.site.register(Humidity, HumidityAdmin)
admin.site.register(Temperature, TemperatureAdmin)
