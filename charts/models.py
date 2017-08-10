# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=80)
    #TODO: force email to be unique
    email = models.EmailField()

    def __str__(self):
        return self.name

class Sprint(models.Model):
    title = models.CharField(max_length=50)
    team = models.ManyToManyField(Person)

    start_date = models.DateField(auto_now_add=true)
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Amount_Progress_Done(models.Model):
    amount = models.FloatField()
    date = models.DateField()

    person = models.ForeignKey(Person)
    sprint = models.ForeignKey(Sprint)

    def __str__(self):
        return str(self.amount)

class Amount_Progress_InReview(models.Model):
    amount = models.FloatField()
    date = models.DateField()

    person = models.ForeignKey(Person)
    sprint = models.ForeignKey(Sprint)

    def __str__(self):
        return str(self.amount)

class Amount_Committed(models.Model):
    amount = models.FloatField()
    date = models.DateField()

    person = models.ForeignKey(Person)
    sprint = models.ForeignKey(Sprint)

    def __str__(self):
        return str(self.amount)

