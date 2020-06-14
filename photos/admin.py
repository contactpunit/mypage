from django.contrib import admin
from .models import Photos


@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'slug', 'publish', 'caption', 'status', 'uploaded', 'updated', 'photo']
