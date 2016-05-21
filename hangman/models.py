from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):   # table class inherits models.Model
    name = models.CharField(max_length=30)  # default lenght = 30
    score = models.IntegerField(default=0)  # default value = 0

    def __unicode__(self):  # __str__ on Python 3
        return "%s: %d" %(self.name, self.score)


class Question(models.Model):
    word = models.CharField(max_length=30)
    hint = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "%s: %s" %(self.word, self.hint)
