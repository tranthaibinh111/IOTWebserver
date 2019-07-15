import uuid

from django.db import models
from .sensor import Sensor


class Temperature(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='temperature_sensor')
    value = models.DecimalField(default=0, max_digits=9, decimal_places=0)
    created_date = models.DateTimeField()
    timestamp = models.IntegerField()

    def __str__(self):
        return '{0}: {1}'.format(str(self.sensor), self.value)

    class Meta:
        unique_together = ('sensor', 'timestamp')
        index_together = ('sensor', 'timestamp')
