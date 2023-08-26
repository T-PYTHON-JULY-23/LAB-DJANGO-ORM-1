from django.db import models

# Create your models here.

class post(models.Model):

    title = models.CharField(max_length=2048)
    description = models.TextField()
    rating = models.IntegerField()
    publish_date = models.DateField()


