from django.db import models

# Create your models here.
class Service(models.Model):

    serviceName = models.CharField(max_length=264 , unique=True)
    imageUrl = models.CharField(max_length=264)
    serviceText = models.CharField(max_length=264)

    def __str__(self):

        return self.serviceName

class Affiliation(models.Model):

    orgName = models.CharField(max_length=264 , unique=True)
    orgDetails = models.CharField(max_length=264)
    orgImg = models.CharField(max_length=264)

    def __str__(self):
        return self.orgName


class Recruiters(models.Model):

    recName = models.CharField(max_length=264 , unique=True)
    recDetails = models.CharField(max_length=264)
    recImg = models.CharField(max_length=264)

    def __str__(self):
        return self.recName
