from django.urls import path
from django.views.generic import RedirectView

from .views import base, add_to_registry, validate_url, issue_registry, dashboard

urlpatterns = [
    path('base/', base),
    path('add/', add_to_registry),
    path('api/validate_url', validate_url),
    path('issue_registry/', issue_registry),
    path('dashboard/', dashboard, name='dashboard'),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
]
