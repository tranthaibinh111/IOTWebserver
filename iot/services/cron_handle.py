import requests
import json

from datetime import datetime
from decimal import Decimal
from django.conf import settings
from django.db.models import Q
from iot.models import *


class CronHandleService:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if CronHandleService.__instance == None:
            CronHandleService()
        return CronHandleService.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CronHandleService.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CronHandleService.__instance = self

    @classmethod
    def handle_temperature_humidity(cls):
        data = CronHandle.objects.filter(
            Q(ishandling=False) &
            Q(sensor__device_type__pk=1)
        )[:100]

        # Lock data
        for cron in data:
            # Update cron status
            cron.ishandling = True
            cron.save()

        # Handle each line
        for cron in data:
            # Send advertisement email
            try:
                # the info was pushed by sensor
                sensor = cron.sensor
                humidity = cron.data_json.get('humidity')
                temperature = cron.data_json.get('temperature')
                timestamp = cron.data_json.get('timestamp')

                # Check humidity data
                if not humidity:
                    if Decimal(humidity):
                        humidity = Decimal('0')
                    else:
                        humidity = Decimal(humidity)
                # Check temperature data
                if not temperature:
                    if Decimal(temperature):
                        temperature = Decimal('0')
                    else:
                        temperature = Decimal(temperature)
                # Check temperature data
                if not timestamp:
                    if datetime.fromtimestamp(timestamp):
                        created_date = datetime.fromtimestamp(timestamp)
                    else:
                        created_date = datetime.now()
                else:
                    created_date = datetime.now()

                # Create humidity history
                Humidity.objects.create(
                    sensor=sensor,
                    value=humidity,
                    created_date=created_date,
                    timestamp=created_date.timestamp()
                )

                # Create temperature history
                Temperature.objects.create(
                    sensor=sensor,
                    value=temperature,
                    created_date=created_date,
                    timestamp=created_date.timestamp()
                )
                # Remove cron when the process is done
                cron.delete()

                if settings.WEBSERVER:
                    # Data to be sent to api
                    payload = {
                        "sensor": sensor.pk,
                        "data_json": json.dumps({
                            "humidity": humidity,
                            "temperature": temperature,
                            "timestamp": created_date.timestamp()
                        })
                    }
                    # Sending post request
                    url = 'http://{0}/iot/cron_handle/'.format(settings.WEBSERVER)
                    headers = {'Authorization': 'Token 7ae10d7a8a8e8263e41852cf804dfc79bce8b502'}
                    h = requests.post(url, data=payload, headers=headers)
                    print("Test: {0}".format(h.content))

            except Exception as ex:
                cron.ishandling = False
                cron.save()
