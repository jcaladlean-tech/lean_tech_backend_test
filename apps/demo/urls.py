from rest_framework import routers

from .views import CarrierViewSet, ShipmentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'carrier', CarrierViewSet)
router.register(r'shipment', ShipmentViewSet)
