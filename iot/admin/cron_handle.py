from django.contrib import admin
from iot.models import *


class CronHandleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sensor_name', 'data_json', 'created_date',)
    ordering = ('-created_date',)
    search_fields = ('sensor.name',)

    def sensor_name(self, obj):
        return obj.sensor.name

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
