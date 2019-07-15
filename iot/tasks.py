from celery import shared_task
from .services import *


@shared_task
def handle_temperature_humidity():
    cron = CronHandleService.get_instance()
    cron.handle_temperature_humidity()
