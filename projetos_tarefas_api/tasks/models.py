from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
