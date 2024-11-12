# mockapp_fintech/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import render
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger schema view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Mockapp Fintech API",
        default_version='v1',
        description="API documentation for Mockapp Fintech platform",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Simple landing page view
def landing_page(request):
    return render(request, 'landing.html')

urlpatterns = [
    # Landing page
    path('', landing_page, name='landing'),  # Add this line for root URL
    
    # Existing URLs
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
