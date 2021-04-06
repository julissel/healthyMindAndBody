from django.views.generic import ListView, DetailView
from useraccounts.models import StudentsGroup, Student


class StudentsGroup(ListView):
    model = StudentsGroup


class Student(DetailView):
    model = Student
