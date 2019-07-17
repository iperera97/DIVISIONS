from django.db import models


class Province(models.Model):

    introduction = models.TextField()
    sinhalaName = models.CharField(max_length=255)
    tamilName = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    featureImage = models.ImageField(
        upload_to='images/provinces/')
    mapUrl = models.CharField(max_length=255)

    def __str__(self):
        return "(#{}) {}".format(self.pk, self.englishName)
