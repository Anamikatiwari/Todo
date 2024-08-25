from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED')
        ('F', 'PENDING')
    ]
        status_choices = [
        ('C', 'COMPLETED')
        ('F', 'PENDING')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 . chices= status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 . chices= status_choices)
    