from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('publisher', on_delete=models.CASCADE)
    pubdate = models.DateField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name  = models.CharField(max_length=50)
    intro = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name