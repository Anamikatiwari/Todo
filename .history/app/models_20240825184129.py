from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED')
        ('F', 'PENDING')
    ]
    priority_choices = [
        ('1', '1️⃣')
        ('2', '2️⃣')
        ('3', 'COMPLETED')
        ('4', 'PENDING')
        ('5', 'COMPLETED')
        ('6', 'PENDING')
        ('7', 'COMPLETED')
        ('8', 'PENDING')
        ('9', 'COMPLETED')
        ('10', '🔟')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 . chices= status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 . chices= status_choices)
    