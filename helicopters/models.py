from django.db import models


# my model
class Helicopter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    amount_of_passengers = models.IntegerField()
    maximum_speed = models.IntegerField()
    price = models.IntegerField()
    objects = models.Manager()  # Object Realetive Mapping - manege your model with many func
