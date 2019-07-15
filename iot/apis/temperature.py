from rest_framework import mixins, viewsets
from iot.models import *
from iot.serializers import *


class TemperatureViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        return Temperature.objects.all()
