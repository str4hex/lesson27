import json

from django.db import models


# Create your models here.

class Ads(models.Model):
    Id = models.IntegerField(max_length=10,primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField(max_length=10)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(max_length=255)


class Cat(models.Model):
    id = models.IntegerField(max_length=10,primary_key=True)
    name = models.CharField(max_length=255)



