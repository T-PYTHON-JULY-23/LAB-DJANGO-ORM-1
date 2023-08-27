from django.db import models

# Create your models here.

class Blog(models.Model):
    class Contents(models.TextChoices):
        Content1="1",'free time'
        Content2="2",'helth '
        Content3="3",'food'
        Content="4",'care and beauty'


    title = models.CharField(max_length=2048)
    Content = models.TextField(max_length=2048 ,choices=Contents.choices)
    category = models.IntegerField()
    publish_date = models.DateField()




