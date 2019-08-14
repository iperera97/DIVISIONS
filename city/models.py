from django.db import models
from district.models import District
from django.shortcuts import reverse


class City(models.Model):

    introduction = models.TextField(blank=True, null=True)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE
    )
    sinhalaName = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    englishName = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    tamilName = models.CharField(
        max_length=255,
        null=True,
        blank=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    featureImage = models.ImageField(
        upload_to='images/city/',
        blank=True,
        null=True)
    mapUrl = models.URLField(
        max_length=255,
        unique=True,
        blank=True,
        null=True)
    postal_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "({}) {}".format(self.pk, self.englishName)

    def get_absolute_url(self):
        return reverse("city:edit", kwargs={"pk": self.pk})
