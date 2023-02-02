from django.db import models


class FillerTextModel(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    text = models.TextField()
    original = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "ダミーテキスト"
