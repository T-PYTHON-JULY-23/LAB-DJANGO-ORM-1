from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=2044)
    content = models.TextField()
    category = models.CharField(max_length=7000)
    publish_date = models.DateTimeField()