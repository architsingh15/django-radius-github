from django.urls import path
from .views import base, add_to_registry, validate_url

urlpatterns = [
    path('base/', base),
    path('add/', add_to_registry),
    path('api/validate_url', validate_url),
]
