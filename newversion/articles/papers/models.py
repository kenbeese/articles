from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Journal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    publisher = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.tag

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author, blank=True, null=True)
    issue_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    journal = models.ForeignKey(Journal, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title
