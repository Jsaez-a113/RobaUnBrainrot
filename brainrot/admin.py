from django.contrib import admin
from .models import BrainrotItem


@admin.register(BrainrotItem)
class BrainrotItemAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")
    search_fields = ("name", "description")
    list_filter = ("created", "updated")