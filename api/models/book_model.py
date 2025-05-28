from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    ISBN = models.CharField(max_length=17, unique=True)
    page_count = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)