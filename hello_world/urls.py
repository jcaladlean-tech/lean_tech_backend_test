from django.urls import include, path
from .views import hello_world_txt, hello_world_json

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('txt', hello_world_txt),
    path('json', hello_world_json),
]