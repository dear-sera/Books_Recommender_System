from django.db import models
from django.db.models.fields import TextField
from ..book_constant import cid_to_cat

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    summary = models.TextField()
    category = models.CharField(max_length=50, choices=tuple(cid_to_cat.items()))
    author = models.CharField(max_length=100)
    src = models.TextField()
