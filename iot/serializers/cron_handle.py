from rest_framework import serializers
from .sensor import SensorSerializer
from iot.models import *


class CronHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronHandle
        fields = ('pk', 'sensor', 'data_json',)
