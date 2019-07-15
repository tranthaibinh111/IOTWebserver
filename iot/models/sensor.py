import uuid

from django.db import models
from mvc.models import *
from .device_type import DeviceType


class Sensor(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_sensor')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_sensor')
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
