from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department_view')

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    due_date = models.DateField(default=timezone.now() + timezone.timedelta(days=1))
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
