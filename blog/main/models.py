from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    category=models.CharField(max_length=10,default='none')
    publish_date =models.DateTimeField()
