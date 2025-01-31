from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True, auto_created=True)
    completed = models.BooleanField(default=False, db_default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.completed}'