from django.db import models

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('LT', 'Literature'),
        ('IT', 'Technology'),
        ('FO', 'Food'),
        ('TR', 'Travel'),
        ('HE', 'Health'),
    ]

    title = models.CharField(max_length=2048, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField()

