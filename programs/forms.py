from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from programs.models import Course


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
