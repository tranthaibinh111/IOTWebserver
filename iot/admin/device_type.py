from django.contrib import admin
from iot.models import *


class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_date', 'modified_by', 'modified_date')
    ordering = ('-pk',)
    search_fields = ('name',)
    readonly_fields = ('created_by', 'created_date', 'modified_by', 'modified_date')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
            obj.modified_by = request.user
        super().save_model(request, obj, form, change)
