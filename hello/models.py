from django.db import models



class PatientInfo(models.Model):
    classify = models.CharField(max_length=50)
    age = models.IntegerField()
    phenotype = models.CharField(max_length=200)
    numbers = models.IntegerField()
    size = models.IntegerField()
    location = models.CharField(max_length=20)
    migration = models.CharField(max_length=6)


