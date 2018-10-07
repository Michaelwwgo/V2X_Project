from django.contrib import admin
from . import models

@admin.register(models.Event)
class EnventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'time',
        'road',
        'detail',
        'creator',
        'created_at',
        'updated_at',
    )
