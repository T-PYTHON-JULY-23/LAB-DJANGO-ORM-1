from django.db import models

# Create your models here.

class post(models.Model):
    
    category_choices=(("Bio" ,"Biography") , ("type" , "type"))

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=128 , choices=category_choices)
    publish_date = models.DateField()


