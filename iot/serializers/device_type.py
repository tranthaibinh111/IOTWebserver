from rest_framework import serializers
from iot.models import *


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('pk', 'name',)
