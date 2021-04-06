from django.urls import path
import programsschedule.views as views


app_name = 'programsschedule'

urlpatterns = [
    path('', views.Schedule.as_view(), name='schedule'),
]
