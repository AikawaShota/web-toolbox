from django.db import models


class FillerTextModel(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    original = models.CharField(max_length=255, null=True, blank=True)
