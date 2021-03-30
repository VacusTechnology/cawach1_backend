from django.db import models


# Create your models here.

class Asset(models.Model):
    studentName = models.CharField(max_length=50)
    tagId = models.CharField(max_length=30, unique=True)
    registrationNo = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15)
    mailId = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)


class AssetHealth(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    lastseen = models.DateTimeField(auto_now=True)
    battery = models.FloatField()
