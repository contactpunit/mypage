from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['category']
