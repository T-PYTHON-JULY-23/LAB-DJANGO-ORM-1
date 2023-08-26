from django.db import models

# Create your models here.

class BlogWebsite(models.Model):

    Category = [
    ('FASHION','Fashion'),
    ('BEAUTY','Beauty'),
    ('TRAVEL','Travel'),
    ('PERSONAL', 'Personal'),
    ('TECH','Tech'),
    ('HEALTH','Health'),
    ('HOME','Home'),
    ('FITNESS','Fitness'),
    ('EDUCATION','Education'),
    ('FOOD','Food'),
    ('ENTERTAINMENT','Entertainment')
]
    
    title = models.CharField(max_length=512)  
    content = models.TextField()
    category = models.CharField(max_length=512, choices= Category) 
    publish_date = models.DateTimeField() 