from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, auto_created=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.completed}'