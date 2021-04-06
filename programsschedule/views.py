from django.shortcuts import render
from django.views.generic import ListView
from programsschedule.models import Schedule


class Schedule(ListView):
    model = Schedule
