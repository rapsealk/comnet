from __future__ import unicode_literals

from django.db import models
# Create your models here.

class User(models.Model):   # table class inherits models.Model
    name = models.CharField(max_length=30)  # default length = 30
    score = models.IntegerField(default=0)  # default value = 0

    def __unicode__(self):  # __str__ on Python 3
        return "%s: %d" %(self.name, self.score)


class Question(models.Model):
    word = models.CharField(max_length=45)
    length = models.IntegerField(default=0)
    hint = models.CharField(max_length=200)
    key = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s: %s" %(self.word, self.hint)


class Counting(models.Model):
    name = models.CharField(max_length=30, default='')
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s: %d" %(self.name, self.count)

class Player(models.Model):
    name = models.CharField(max_length=30, default='default')
    #number = models.IntegerField(default=0)
    init = models.IntegerField(default=1)
    lives = models.IntegerField(default=8)
    done = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s(%d)_init:%d" %(self.name, self.lives, self.init)


class Quiz(models.Model):
    key = models.CharField(max_length=10)
    answer = models.CharField(max_length=45, default='')
    current = models.CharField(max_length=45, default='')
    lives = models.IntegerField(default=8)

    def __unicode__(self):
        return "%s(%s)" %(self.current, self.answer)
