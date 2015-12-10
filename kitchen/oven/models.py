__author__ = 'hieutran'

from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=32, default="", null=False)
    note = models.TextField(null=True, default="")


class Contractor(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    location = models.CharField(max_length=128, default="", null=False)
    component = models.CharField(max_length=128, default="", null=False)
    note = models.TextField(null=True, default="")


class Assignment(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    contractor = models.CharField(max_length=128, default="", null=False)
    component = models.IntegerField(null=False, default=1)
    deadline = models.DateTimeField(null=False, auto_now_add=True)
    requirement = models.TextField(null=True, default="")
    rating = models.SmallIntegerField(null=False, default=0)


class ContractorRating(models.Model):
    contractor = models.CharField(max_length=128, default="", null=False)
    rating = models.SmallIntegerField(null=False, default=0)


class CustomerFeedback(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    phone = models.CharField(max_length=128, default="", null=False)
    email = models.CharField(max_length=128, default="", null=False)
    social_number = models.CharField(max_length=128, default="", null=False)
    address = models.CharField(max_length=128, default="", null=False)
    component = models.IntegerField(null=False, default=1)
    problem = models.TextField(null=True, default="")
    rating = models.SmallIntegerField(null=False, default=0)


class Customer(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
    phone = models.CharField(max_length=128, default="", null=False)
    email = models.CharField(max_length=128, default="", null=False)
    city = models.CharField(max_length=128, default="", null=False)
    address = models.CharField(max_length=128, default="", null=False)


class City(models.Model):
    name = models.CharField(max_length=128, default="", null=False)
