import operator
from functools import reduce

from django.db.models import Q
from rest_framework import viewsets
from .serializers import CarrierSerializer, ShipmentSerializer
from .models import Carrier, Shipment


class CarrierViewSet(viewsets.ModelViewSet):
    """docstring for CarrierViewSet"""
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(CarrierViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Carrier.objects.all()

        return queryset


class ShipmentViewSet(viewsets.ModelViewSet):
    """docstring for CarrierViewSet"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(ShipmentViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        q = "" if not self.request.GET.get('q') else self.request.GET.get('q')

        list_q = debug_params(q)

        queryset = Shipment.objects.all()

        fields_look = [
            'status__icontains',
            'carrier_id__name__icontains',
            'origin_state__icontains',
            'origin_city__icontains',
            'destination_state__icontains',
            'destination_city__icontains',
        ]

        for query_term in list_q:
            or_queries = [Q(**{field_look: query_term})
                          for field_look in fields_look]
            queryset = queryset.filter(reduce(operator.or_, or_queries))

        return queryset


def debug_params(param):
    list_p = param.split(' ')
    return list(
        filter(
            lambda x: x != '' and x !=
                      'the' and x != 'that' and x != 'but', list_p))
