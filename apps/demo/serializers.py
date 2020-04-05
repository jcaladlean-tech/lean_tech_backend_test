from rest_framework import serializers
from .models import Carrier, Shipment


class CarrierSerializer(serializers.ModelSerializer):
    """docstring for CarrierSerializer"""

    class Meta:
        model = Carrier
        fields = (
            'id', 'scac', 'name', 'MC', 'DOT', 'FEIN',
        )
        read_only_fields = ('id',)


class ShipmentSerializer(serializers.ModelSerializer):
    """docstring for ShipmentSerializer"""
    carrier_data = CarrierSerializer(read_only=True, source='carrier_id')

    class Meta:
        model = Shipment
        fields = (
            'id', 'date', 'origin_country', 'origin_state', 'origin_city', 'destination_country', 'destination_state',
            'destination_city', 'pick_up_date', 'delivery_date', 'status', 'carrier_rate', 'carrier_id', 'carrier_data'
        )
        read_only_fields = ('id',)

