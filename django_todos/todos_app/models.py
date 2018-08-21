from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


class Todo(TimeStampedModel):
    class Meta:
        ordering = ['-created']

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.owner)
