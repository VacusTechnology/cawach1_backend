from django.db import models
from asset.models import Asset


class ContactTracing(models.Model):
    tag1 = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="tag1id")
    tag2 = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="tag2id")
    lastSeen = models.DateTimeField(auto_now=True)
    epochTime = models.FloatField()

