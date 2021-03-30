from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from asset.models import Asset

""""""


class DailyReport(models.Model):
    tagId = models.ForeignKey(Asset, on_delete=models.CASCADE)
    lastSeen = models.CharField(max_length=30)
    inTime = models.CharField(max_length=30)


class AttendanceSheet(models.Model):
    tagId = models.ForeignKey(Asset, on_delete=models.CASCADE)
    day_1 = models.CharField(max_length=2, null=False)
    day_2 = models.CharField(max_length=2, null=False)
    day_3 = models.CharField(max_length=2, null=False)
    day_4 = models.CharField(max_length=2, null=False)
    day_5 = models.CharField(max_length=2, null=False)
    day_6 = models.CharField(max_length=2, null=False)
    day_7 = models.CharField(max_length=2, null=False)
    day_8 = models.CharField(max_length=2, null=False)
    day_9 = models.CharField(max_length=2, null=False)
    day_10 = models.CharField(max_length=2, null=False)
    day_11 = models.CharField(max_length=2, null=False)
    day_12 = models.CharField(max_length=2, null=False)
    day_13 = models.CharField(max_length=2, null=False)
    day_14 = models.CharField(max_length=2, null=False)
    day_15 = models.CharField(max_length=2, null=False)
    day_16 = models.CharField(max_length=2, null=False)
    day_17 = models.CharField(max_length=2, null=False)
    day_18 = models.CharField(max_length=2, null=False)
    day_19 = models.CharField(max_length=2, null=False)
    day_20 = models.CharField(max_length=2, null=False)
    day_21 = models.CharField(max_length=2, null=False)
    day_22 = models.CharField(max_length=2, null=False)
    day_23 = models.CharField(max_length=2, null=False)
    day_24 = models.CharField(max_length=2, null=False)
    day_25 = models.CharField(max_length=2, null=False)
    day_26 = models.CharField(max_length=2, null=False)
    day_27 = models.CharField(max_length=2, null=False)
    day_28 = models.CharField(max_length=2, null=False)
    day_29 = models.CharField(max_length=2, null=False)
    day_30 = models.CharField(max_length=2, null=False)
    day_31 = models.CharField(max_length=2, null=False)
