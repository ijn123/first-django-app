from django.db import models

# Create your models here.
class Vehicles(models.Model):
    auto_number = models.CharField(max_length=20)

class Coordinates(models.Model):
    vehicle = models.ForeignKey(Vehicles)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)
    coordinate_timestamp = models.DateTimeField()