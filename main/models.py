from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class University(models.Model):

    university = models.CharField(max_length=255) 

    def __str__(self):
        return self.university

class Specialty(models.Model):

    title = models.CharField(max_length=255)
    university = models.ManyToManyField(University)


    def __str__(self):
        return self.title