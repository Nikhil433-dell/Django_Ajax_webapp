from django.db import models
from django.http import HttpResponse
from django.urls import reverse

# Create your models here.



class Vehicle(models.Model):
    speed = models.IntegerField()
    avg_speed = models.IntegerField()
    engine_status = models.CharField(max_length=100)
    fuel_level = models.CharField(max_length=100)
    temp = models.IntegerField()

    # def get_absolute_url(self):
    #     return HttpResponse("Vehicle Created")
    