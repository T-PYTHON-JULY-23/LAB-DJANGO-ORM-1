from django.db import models

# Create your models here.
class Post(models.Model):
    
    

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20)
    publish_date = models.DateTimeField()

   

