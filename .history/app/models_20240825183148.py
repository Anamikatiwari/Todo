from django.db import models

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ""
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    