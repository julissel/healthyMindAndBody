from django.contrib import admin
from .models import Course, Category


admin.site.register(Category)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'status', 'short_description'
    list_display_links = 'id', 'name', 'short_description'
    list_filter = 'status',
