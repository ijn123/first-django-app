from django.db import models

# Create your models here.
class Vehicle(models.Model):
    auto_number = models.CharField(max_length=20)
    # pub_date = models.DateTimeField('date published')


class Coordinates(models.Model):
    Vehicle_id = models.ForeignKey(Question)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)
    coordinate_date = models.models.DateField()
