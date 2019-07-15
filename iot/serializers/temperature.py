from rest_framework import serializers
from .sensor import SensorSerializer
from iot.models import *


class TemperatureSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(many=False, read_only=True)

    class Meta:
        model = Temperature
        fields = ('pk', 'sensor', 'value', 'created_date', 'timestamp')
