from django.db import models

class Model1(models.Model):
    field1 = models.CharField(max_length=100)

class Model2(models.Model):
    field2 = models.IntegerField()

class Model3(models.Model):
    field3 = models.BooleanField(default=False)
