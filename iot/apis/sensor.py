from rest_framework import mixins, viewsets
from iot.models import *
from iot.serializers import *


class SensorViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = SensorSerializer

    def get_queryset(self):
        return Sensor.objects.all()
