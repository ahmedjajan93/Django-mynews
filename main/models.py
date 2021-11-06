from __future__ import unicode_literals
from django.db import models

class Main(models.Model):
    
    name = models.CharField(default='-', max_length=200)
    about = models.TextField(default='-')
    fb = models.CharField(default='-', max_length=200)
    tw = models.CharField(default='-', max_length=200)
    yt = models.CharField(default='-', max_length=200)
    set_name = models.CharField(default='-', max_length=200)
    tell = models.CharField(default='-', max_length=200)
    link = models.CharField(default='-', max_length=200)

    def __str__(self):
        return self.set_name +'-'+ str(self.pk)
