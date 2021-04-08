from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from programs.models import Course


class CoursesListView(ListView):
    model = Course


class CourseItem(DetailView):
    model = Course


# FBV
def index(request):
    return render(request, 'programs/index.html')


class CourseCreateView(CreateView):
    model = Course
    template_name = 'programs/course_create.html'
    success_url = reverse_lazy('programs:courses')
    # success_url = '/courses/'
    fields = '__all__'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'programs/course_update.html'
    success_url = reverse_lazy('programs:courses')
    fields = ['name', 'description', 'status', 'category']


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('programs:courses')
    template_name = 'programs/course_delete.html'
