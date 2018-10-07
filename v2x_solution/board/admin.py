from django.contrib import admin
from . import models

@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentCarAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
        'creator',
        'created_at',
        'updated_at',
    )

