from django.db import models

from utils.models import Timestamp


class Todo(Timestamp):
    title = models.CharField(max_length=100, default='Your Task')
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
