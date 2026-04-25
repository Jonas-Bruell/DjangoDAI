from django.db import models

# Create your models here.

class WorpData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    beginsnelheid_km_per_h = models.FloatField()
    beginhoek_graden = models.FloatField()
    vliegtijd_seconden = models.FloatField()
    vliegafstand_meter = models.FloatField()