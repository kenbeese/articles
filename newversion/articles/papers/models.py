from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kana = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.tag

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    authors = models.ManyToManyField(Author, null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    bookfile = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
