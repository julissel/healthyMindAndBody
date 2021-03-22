from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'id', 'start_at', 'end_till', 'group', 'trainer'
    list_display_links = 'id', 'group'
    list_filter = 'group', 'trainer'
