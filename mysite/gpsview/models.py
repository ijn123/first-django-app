from django.db import models

# Create your models here.
class Vehicles(models.Model):
    auto_number = models.CharField(max_length=20)

class Coordinates(models.Model):
    vehicle_id = models.ForeignKey(Vehicles)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    coordinate_date = models.DateTimeField()
