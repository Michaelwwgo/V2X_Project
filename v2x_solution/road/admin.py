from django.contrib import admin
from . import models

@admin.register(models.Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'speed',
        'created_at',
        'updated_at',
    )

@admin.register(models.Situation)
class SituationAdmin(admin.ModelAdmin):

    list_display = (
        'road',
        'isimpassable',
        'message',
        'startTime',
        'endTime',
        'creator',
        'created_at',
        'updated_at',
    )
