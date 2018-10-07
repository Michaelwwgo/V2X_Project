from django.contrib import admin
from . import models

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'isFind',
        'created_at',
        'updated_at',
    )

@admin.register(models.CriminalCar)
class CriminalCarAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.PostCar)
class PostCarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'owner',
        'created_at',
        'updated_at',
    )