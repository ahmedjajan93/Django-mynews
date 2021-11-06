from __future__ import unicode_literals
from django.db import models
import datetime

class News(models.Model):

    name = models.CharField(max_length=200)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.DateField()
    pic = models.TextField()
    writer = models.TextField(max_length=50)

    def __str__(self):
        return self.name +'-'+ str(self.pk)