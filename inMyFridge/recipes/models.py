from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recipe (models.Model):
    name = models.CharField(max_length=150)
    date_published = models.DateTimeField()
    description = models.TextField()
    