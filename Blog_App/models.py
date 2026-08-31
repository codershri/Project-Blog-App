from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
