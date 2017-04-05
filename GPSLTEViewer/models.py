from django.db import models

# Create your models here.
class Pegel (models.Model):
    time = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField()
    lteband = models.FloatField()
    ltebw = models.FloatField()
    rxchan = models.FloatField()
    txchan = models.FloatField()
    emmstate = models.CharField(max_length=200)
    rccstate = models.CharField(max_length=200)
    imsstate = models.CharField(max_length=200)

    text = models.TextField()