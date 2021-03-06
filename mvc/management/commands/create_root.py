#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from mvc.models import User


class Command(BaseCommand):
    help = 'Create root for system'

    def handle(self, *args, **options):
        try:
            if not User.objects.filter(email="internet_of_things@grad.uit.edu.vn").exists():
                print("Begin create root")
                user = User.objects.create_user(
                    first_name="root",
                    last_name="",
                    username="internetofthings",
                    password="esp8266dht22",
                    email="internet_of_things@grad.uit.edu.vn",
                    is_superuser=True,
                    is_staff=True,
                    timezone="Asia/Ho_Chi_Minh"
                )
                print(user)
                print("End!")
        except Exception as ex:
            raise ex
