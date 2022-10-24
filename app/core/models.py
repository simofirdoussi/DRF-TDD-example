"""
Core app models.
"""
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    descritpion = models.TextField()

    def __str__(self):
        return self.name

