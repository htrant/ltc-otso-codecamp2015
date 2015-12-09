__author__ = 'hieutran'

from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=32, default="", null=False)
    note = models.TextField(null=True, default="")


class Contractor(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    location = models.CharField(max_length=128, default="", null=False)
    component = models.ForeignKey(Component)
    note = models.TextField(null=True, default="")


class Assignment(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    contractor = models.ForeignKey(Contractor)
    deadline = models.DateTimeField(null=False, auto_now_add=True)
    requirement = models.TextField(null=True, default="")
