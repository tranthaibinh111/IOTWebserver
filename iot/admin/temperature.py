from django.contrib import admin
from iot.models import *


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sensor_name', 'value', 'created_date',)
    ordering = ('-timestamp',)
    search_fields = ('sensor.name',)
    readonly_fields = ('timestamp',)

    def sensor_name(self, obj):
        return obj.sensor.name

    def save_model(self, request, obj, form, change):
        obj.timestamp = obj.created_date.timestamp()
        super().save_model(request, obj, form, change)
