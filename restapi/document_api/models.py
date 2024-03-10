from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    status = models.CharField(max_length = 20, choices = [('draft', 'Draft'), ("published","PUBLISHED",) ])

