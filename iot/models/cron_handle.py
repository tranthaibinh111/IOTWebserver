import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from .sensor import Sensor

class CronHandle(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='cron_handle_sensor')
    data_json = JSONField()
    ishandling = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}: {1}'.format(self.created_date, str(self.sensor))

    class Meta:
        index_together = ('created_date',)
