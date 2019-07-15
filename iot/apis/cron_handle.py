from rest_framework import mixins, viewsets
from iot.models import *
from iot.serializers import *


class CronHandleViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = CronHandleSerializer

    def get_queryset(self):
        return CronHandle.objects.all()
