from rest_framework import serializers
from .device_type import DeviceTypeSerializer
from iot.models import *


class SensorSerializer(serializers.ModelSerializer):
    device_type = DeviceTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Sensor
        fields = ('pk', 'name', 'device_type',)
