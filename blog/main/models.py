from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=2048)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")