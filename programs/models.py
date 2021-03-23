from django.db import models
from django.template.defaultfilters import truncatechars


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Category", help_text="enter category name")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ["name"]


class Course(models.Model):
    DRAFT = 'd'
    WORKS = 'w'
    ARCHIVED = 'a'
    STATUSES = (
        (DRAFT, 'course is in the draft'),
        (WORKS, 'course is working'),
        (ARCHIVED, 'course is in the archive'),
        )
    name = models.CharField(max_length=100, verbose_name="Course", help_text="add the name")
    description = models.TextField(blank=True, verbose_name="Course description",
                                   help_text="add some description")
    last_changed = models.DateTimeField(auto_now=True, verbose_name="Date of change")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    status = models.CharField(max_length=1, choices=STATUSES, default=DRAFT, verbose_name="Status")

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"

    @property
    def is_draft(self):
        return self.status == self.DRAFT

    @property
    def is_working(self):
        return self.status == self.WORKS

    @property
    def is_archive(self):
        return self.status == self.ARCHIVED

    @property
    def short_description(self):
        return truncatechars(self.description, 25)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-last_changed', 'name']
