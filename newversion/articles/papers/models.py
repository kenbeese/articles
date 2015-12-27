from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Journal(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, null=True)

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)
    # authors = models.ManyToManyField(Author)
    # issue_date = models.DateField(null=True)
    # tag = models.ManyToManyField(Tag)
    # journal = models.ForeignKey(Journal)
    # note = models.CharField(max_length=255, null=True)
