from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

     title = models.CharField(max_length=50)
     description = models.TextField(blank=True)

     is_completed = models.BooleanField(default=False)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)