from django.db import models
from django.shortcuts import reverse


class Province(models.Model):

    introduction = models.TextField(blank=True, null=True)
    sinhalaName = models.CharField(max_length=255, unique=True)
    englishName = models.CharField(max_length=255, unique=True)
    tamilName = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    featureImage = models.ImageField(
        upload_to='images/provinces/', blank=True, null=True)
    mapUrl = models.URLField(
        max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return "(#{}) {}".format(self.pk, self.englishName)

    def get_absolute_url(self):
        return reverse("provinces:edit", kwargs={"pk": self.pk})
