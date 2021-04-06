from django.shortcuts import render
from django.views.generic import ListView, DetailView
from programs.models import Course


class CoursesListView(ListView):
    model = Course


class CourseItem(DetailView):
    model = Course


# FBV
def index(request):
    return render(request, 'programs/index.html')
