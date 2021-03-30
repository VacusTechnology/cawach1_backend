from django.db import models


# Create your models here.

class Gateway(models.Model):
    gatewayId = models.CharField(max_length=40, unique=True)
    gatewayName = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
