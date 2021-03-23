from django.db import models
from programs.models import Course


class SiteUser(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='nickname', help_text='enter nickname')
    first_name = models.CharField(max_length=30, verbose_name='first name')
    last_name = models.CharField(max_length=60, verbose_name='last name')
    email = models.EmailField(blank=True, verbose_name='email address')
    date_registration = models.DateTimeField(auto_now_add=True, verbose_name='date registration')
    location = models.CharField(max_length=30, blank=True, verbose_name="Location", help_text="add Country")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Date of Birth")

    def __str__(self):
        return f"User '{self.name}'. {self.last_name} {self.first_name}."


class StudentsGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name="Students group", help_text="enter group name")
    entry_date = models.DateField(verbose_name="Entry date")
    graduation_date = models.DateField(verbose_name="Graduation date")

    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"


class Trainer(models.Model):
    user_id = models.OneToOneField(SiteUser, on_delete=models.PROTECT)
    is_main_mentor = models.BooleanField(default=False)


class Student(models.Model):
    user_id = models.OneToOneField(SiteUser, on_delete=models.PROTECT)
    groups = models.ManyToManyField(StudentsGroup)
