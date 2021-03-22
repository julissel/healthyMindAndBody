from django.db import models
from useraccounts.models import Trainer, StudentsGroup


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)
    group = models.ForeignKey(StudentsGroup, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, blank=True, verbose_name="event details",
                                   help_text="add event description")
    start_at = models.DateTimeField(null=False, blank=False, verbose_name="Start date")
    end_till = models.DateTimeField(null=False, blank=False, verbose_name="End till")

    def __str__(self):
        return f"Event '{self.description}' will be held from {self.start_at} till {self.end_till}"

    class Meta:
        ordering = ['start_at', 'end_till']
