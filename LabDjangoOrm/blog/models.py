from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=2067)
    content = models.TextField()
    category = models.CharField(max_length=2048)
    publish_date = models.DateTimeField()
