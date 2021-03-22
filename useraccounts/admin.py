from django.contrib import admin
from .models import StudentsGroup, Student, Trainer, SiteUser


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = 'name', 'entry_date', 'graduation_date', 'course'


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'first_name', 'last_name', 'location', 'date_registration'
    list_display_links = 'name',
    ordering = '-date_registration',
    list_filter = ('location',)


admin.site.register(Trainer)
admin.site.register(Student)
