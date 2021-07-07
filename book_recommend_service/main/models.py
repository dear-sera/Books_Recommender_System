from django.db import models

# Create your models here.
class BestSeller(models.Model):
    title = models.TextField()
    author = models.TextField()
    link = models.URLField()
