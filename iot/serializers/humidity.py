from rest_framework import serializers
from .sensor import SensorSerializer
from iot.models import *


class HumiditySerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(many=False, read_only=True)

    class Meta:
        model = Humidity
        fields = ('pk', 'sensor', 'value', 'created_date', 'timestamp')
