from django.db import models


class Carrier(models.Model):
    """docstring for Carrier"""
    scac = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    MC = models.IntegerField(null=True, blank=True)
    DOT = models.IntegerField(null=True, blank=True)
    FEIN = models.IntegerField(null=True, blank=True)


class Shipment(models.Model):
    """docstring for Shipment"""
    date = models.DateTimeField(auto_now_add=True)
    origin_country = models.CharField(max_length=30)
    origin_state = models.CharField(max_length=30)
    origin_city = models.CharField(max_length=30)
    destination_country = models.CharField(max_length=30)
    destination_state = models.CharField(max_length=30)
    destination_city = models.CharField(max_length=30)
    pick_up_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)
    carrier_rate = models.DecimalField(max_digits=20, decimal_places=2)
    carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)
