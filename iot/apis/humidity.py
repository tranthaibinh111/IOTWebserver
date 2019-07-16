from rest_framework import mixins, viewsets
from iot.models import *
from iot.serializers import *


class HumidityViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = HumiditySerializer

    def get_queryset(self):
        return Humidity.objects.all().order_by('-timestamp')
