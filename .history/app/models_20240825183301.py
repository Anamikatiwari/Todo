from django.db import models

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED')
        ('F', 'PENDING')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2.chices= status_)
    