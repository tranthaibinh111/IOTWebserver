from django.contrib import admin
from iot.models import *


class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'kind', 'created_by', 'created_date', 'modified_by', 'modified_date')
    ordering = ('-modified_date',)
    search_fields = ('name',)
    readonly_fields = ('created_by', 'created_date', 'modified_by', 'modified_date')

    def kind(self, obj):
        return obj.device_type.name

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
            obj.modified_by = request.user
        super().save_model(request, obj, form, change)
